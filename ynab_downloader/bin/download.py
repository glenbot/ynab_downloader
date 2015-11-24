import logging
from datetime import datetime, date

import click

from ..utils import get_driver, configure_log
from ..settings import DRIVER_PATH

now = datetime.now()
logger = logging.getLogger(__name__)


class StoredAccountChoice(click.Choice):
    def convert(self, value, param, ctx):
        value = super(StoredAccountChoice, self).convert(value, param, ctx)
        ctx.obj['account_type'] = value
        return value


class OptionalAccountPrompt(click.Option):
    def prompt_for_value(self, ctx):
        account_type = ctx.obj.get('account_type')
        if account_type == 'singlecc':
            return
        return super(OptionalAccountPrompt, self).prompt_for_value(ctx)


@click.group()
@click.option('--logging', default='INFO', help='Logging level.')
@click.pass_context
def main(ctx, logging):
    ctx.obj = {}
    ctx.obj['driver_path'] = DRIVER_PATH
    configure_log(logging)


@main.command()
@click.option(
    '--username', prompt=True, help='Your Chase bank online username.')
@click.option(
    '--password', prompt=True, hide_input=True,
    help='Your Chase bank online password.'
)
@click.option(
    '--account_type', type=StoredAccountChoice(['cc', 'singlecc', 'checking']), default='cc',
    help='The type of account you want data from. Used for traversing different download areas. Use "singlecc" if you only have one credit card account with chase.',
    show_default=True
)
@click.option(
    '--account_id', cls=OptionalAccountPrompt, prompt=True, hide_input=True,
    help='Account id. Used to match select boxes on the UI.'
)
@click.option(
    '--from_date', default=date(now.year, now.month, 1).strftime('%m/%d/%Y'),
    help='Transactions from this date.',
    show_default=True
)
@click.option(
    '--to_date', default=now.strftime('%m/%d/%Y'),
    help='Transactions to this date.',
    show_default=True
)
@click.option(
    '--format', type=click.Choice(['QFX', 'CSV']), default='QFX',
    help='Output format of the account export.',
    show_default=True
)
@click.pass_context
def chase(ctx, *args, **kwargs):
    from ..base import ChaseDownloader
    driver_path = ctx.obj['driver_path']
    driver = get_driver(driver_path)

    print(kwargs)
    return
    try:
        chase_downloader = ChaseDownloader(driver, kwargs)
        chase_downloader.run()
    except KeyboardInterrupt:
        driver.close()
    except Exception:
        driver.close()
        raise


@main.command()
@click.option(
    '--username', prompt=True, help='Your Bank of America online username.')
@click.option(
    '--password', prompt=True, hide_input=True,
    help='Your Bank of America online password.'
)
@click.option(
    '--account_name', prompt=True, hide_input=True,
    help='Case sensitive. Selects the account to download statements from.'
)
@click.option(
    '--from_date',
    help='Transactions from this date. Default: Current transaction period'
)
@click.option(
    '--to_date', default=now.strftime('%m/%d/%Y'),
    help='Transactions to this date. Default: Current transaction period'
)
@click.option(
    '--format', type=click.Choice(['qfx', 'qif2', 'qif4', 'csv', 'txt']), default='qfx',
    help='Output format of the account export.',
    show_default=True
)
@click.pass_context
def bofa(ctx, *args, **kwargs):
    from ..base import BofaDownloader
    driver_path = ctx.obj['driver_path']
    driver = get_driver(driver_path)

    try:
        bofa_downloader = BofaDownloader(driver, kwargs)
        bofa_downloader.run()
    except KeyboardInterrupt:
        driver.close()
    except Exception:
        driver.close()
        raise
