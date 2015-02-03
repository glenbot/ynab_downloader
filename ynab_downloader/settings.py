import os

ROOT = os.path.abspath(os.path.dirname(__file__))

# Chrome driver
DRIVER_PATH = os.path.join(ROOT, 'driver', 'chromedriver')

# Implicitly wait X seconds for DOM to load
SELENIUM_WAIT = 15

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'format': '%(asctime)s %(levelname)s %(name)s %(lineno)d %(processName)s %(message)s',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'level': 'INFO',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'selenium.webdriver.remote.remote_connection': {
            'level': 'CRITICAL',
            'propagate': False
        }
    }
}

# Chase Bank Settings
CHASE_SETTINGS = {
    'url': 'https://www.chase.com',
    'commands': {
        'cc': [
            {
                'selector': 'usr_name_home',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{username}'
            },
            {
                'selector': 'usr_password_home',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{password}'
            },
            {
                'selector': 'a[data-pt-name="unknwnlogin"]',
                'selector_type': 'css',
                'type': 'click'
            },
            {
                'selector': 'Go_to_Customer_Center',
                'selector_type': 'id',
                'type': 'click'
            },
            {
                'selector': 'a[name="RelatedActivity"]',
                'selector_type': 'css',
                'type': 'click'
            },
            {
                'selector': 'AI',
                'selector_type': 'id',
                'type': 'select',
                'value': '{account_id}'
            },
            {
                'selector': 'input[value="Next"]',
                'selector_type': 'css',
                'type': 'click'
            },
            {
                'selector': 'SelectDateRange',
                'selector_type': 'id',
                'type': 'click'
            },
            {
                'selector': 'FromDate_Value',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{from_date}'
            },
            {
                'selector': 'ToDate_Value',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{to_date}'
            },
            {
                'selector': 'DownloadType',
                'selector_type': 'id',
                'type': 'select',
                'value': '{format}'
            },
            {
                'selector': 'BtnDownloadActivity',
                'selector_type': 'id',
                'type': 'click'
            }
        ],
        'checking': [
            {
                'selector': 'usr_name_home',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{username}'
            },
            {
                'selector': 'usr_password_home',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{password}'
            },
            {
                'selector': 'a[data-pt-name="unknwnlogin"]',
                'selector_type': 'css',
                'type': 'click'
            },
            {
                'selector': 'Go_to_Customer_Center',
                'selector_type': 'id',
                'type': 'click'
            },
            {
                'selector': 'Activate Quicken, QuickBooks, etc.',
                'selector_type': 'link_text',
                'type': 'click'
            },
            {
                'selector': 'DownloadNowRadioButton',
                'selector_type': 'id',
                'type': 'click'
            },
            {
                'selector': 'ContinueButton',
                'selector_type': 'id',
                'type': 'click'
            },
            {
                'selector': 'UserAccounts',
                'selector_type': 'id',
                'type': 'select',
                'value': '{account_id}'
            },
            {
                'selector': 'SelectDateRange',
                'selector_type': 'id',
                'type': 'click'
            },
            {
                'selector': 'FromDate_Value',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{from_date}'
            },
            {
                'selector': 'ToDate_Value',
                'selector_type': 'id',
                'type': 'fill',
                'value': '{to_date}'
            },
            {
                'selector': 'DownloadTypes',
                'selector_type': 'id',
                'type': 'select',
                'value': '{format}'
            },
            {
                'selector': 'BtnDownloadActivity',
                'selector_type': 'id',
                'type': 'click'
            }
        ]
    }
}
