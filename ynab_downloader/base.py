import logging

from .settings import BOFA_SETTINGS, CHASE_SETTINGS
from selenium.common.exceptions import NoSuchElementException

logger = logging.getLogger(__name__)


class BaseChromeDownloader(object):
    """Base object with helpers for traversing the UI"""
    settings = None

    def __init__(self, driver, params):
        """Initialize

        :param driver: the initialized selenium driver
        :param dict params: the params sent from the command line
        """
        self.driver = driver
        self.params = params
        self.log = logger

    @property
    def commands(self):
        """Get a list of commands to run. Subclasses should implement this"""
        return []

    def click(self, element):
        """Click an element"""
        # this is a hack specifically for the chrome when an element
        # too far down the page and the scroll to element doesn't work
        self.driver.execute_script('arguments[0].click();', element)

    def fill(self, element, value):
        """Put a value into an input field

        :param element: the selenium element
        :param str value: the value of the element
        """
        element.send_keys(value)

    def select(self, element, value):
        """Select a value from a dropdown

        :param element: the selenium element
        :param str value: the value of the element
        """
        for option in element.find_elements_by_tag_name("option"):
            if option.get_attribute("value") == value:
                option.click()

    def run(self):
        # initialize the url
        self.driver.get(self.settings['url'])

        for command in self.commands:
            selector = command['selector'].format(**self.params)
            selector_type = command['selector_type']
            _type = command.get('type')

            is_error = command.get('is_error', False)

            value, element = None, None
            self.log.debug('Selector: {}, Selector Type: {}, type: {}'.format(
                selector,
                selector_type,
                _type
            ))

            # check for a value and format
            if 'value' in command:
                value = command['value'].format(**self.params)

            # get the required element
            if selector_type == 'id':
                try:
                    element = self.driver.find_element_by_id(selector)
                except NoSuchElementException:
                    continue

            if selector_type == 'css':
                element = self.driver.find_element_by_css_selector(selector)
            if selector_type == 'tag':
                element = self.driver.find_element_by_tag_name(selector)
            if selector_type == 'link_text':
                element = self.driver.find_element_by_link_text(selector)

            if element and is_error:
                self.log.warning('Error occured. For more info, view browser.')
                return

            self.log.debug('Tag Name: {}, Text: {}'.format(
                element.tag_name,
                element.text
            ))

            if _type == 'fill':
                self.fill(element, value)
            if _type == 'click':
                self.click(element)
            if _type == 'select':
                self.select(element, value)

        self.driver.close()


class ChaseDownloader(BaseChromeDownloader):
    settings = CHASE_SETTINGS

    @property
    def commands(self):
        return self.settings['commands'][self.params['account_type']]


class BofaDownloader(BaseChromeDownloader):
    settings = BOFA_SETTINGS

    @property
    def commands(self):
        return self.settings['commands']
