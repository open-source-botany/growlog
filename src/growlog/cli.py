"""
Module that contains the command line app.

Why does this file exist, and why not put this in __main__?

  You might be tempted to import things from __main__ later, but that will cause
  problems: the code will get executed twice:

  - When you run `python -m growlog` python will execute
    ``__main__.py`` as a script. That means there won't be any
    ``growlog.__main__`` in ``sys.modules``.
  - When you import __main__ it will get executed again (as a module) because
    there's no ``growlog.__main__`` in ``sys.modules``.

  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""
from datetime import datetime

import click

from growlog.main import add_to_growlog
from growlog.main import create_growlog
from growlog.main import load_growlog
from growlog.main import print_growlog


@click.command()
def main():
    growlog = load_growlog()
    if growlog:
        click.echo('Here is your current growlog:\n')
        print_growlog(growlog)
    else:
        click.echo('No growlog found, creating a new one!\n\n')
        create_growlog()
        new_crop()


def new_crop():
    click.echo('**************')
    click.echo('Add a new crop:')
    click.echo('**************')
    crop_data = {}
    crop_data['name'] = click.prompt('What type of plant is this?')
    crop_data['environment'] = click.prompt(
        'Grown outdoor or indoor?', default='outdoor')
    default_date = datetime.today().strftime('%m-%d-%Y')
    crop_data['start_date'] = click.prompt(
        'What is the start date? (dd-mm-yy)', default=default_date)
    crop_data['qty'] = click.prompt('Quantity?', default=1)
    crop_data['notes'] = click.prompt('Notes?')
    add_to_growlog(crop_data)
