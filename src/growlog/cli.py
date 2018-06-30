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
from growlog.main import delete_crop_from_growlog
from growlog.main import load_growlog
from growlog.main import print_growlog
from growlog.main import update_crop_in_growlog


@click.command()
@click.option('--add', is_flag=True, help='Add a crop to your growlog')
@click.option('--update', is_flag=True, help='Update a crop in your growlog')
@click.option('--remove', is_flag=True, help='Remove a crop from your growlog')
def main(add, update, remove):
    growlog = load_growlog()
    if growlog:
        print_growlog(growlog)
        if add:
            new_crop()
        elif update:
            update_crop()
        elif remove:
            delete_crop()
    else:
        click.echo('No growlog found, creating a new one!\n')
        create_growlog()
        new_crop()


def new_crop():
    click.echo('**************')
    click.echo('Add a new crop:')
    click.echo('**************')
    crop_data = {}
    crop_data['name'] = click.prompt('What type of plant is this?')
    crop_data['environment'] = click.prompt(
        'Grown outdoor or indoor?', default='outdoor',
        type=click.Choice(['outdoor', 'indoor']))
    default_date = datetime.today().strftime('%m-%d-%Y')
    crop_data['start_date'] = click.prompt(
        'What is the start date? (dd-mm-yy)', default=default_date)
    crop_data['qty'] = click.prompt(
        'Quantity?', default=1, type=click.IntRange(min=1))
    crop_data['notes'] = click.prompt('Notes?')
    add_to_growlog(crop_data)


def update_crop():
    growlog = load_growlog()
    if not growlog:
        click.echo('No growlog found')
        return
    names = [crop.name for crop in growlog]
    name = click.prompt('Which crop do you want to update?', type=click.Choice(names))
    key = click.prompt('Which field do you want to update?', type=click.Choice(growlog[0].to_dict().keys()))
    val = click.prompt('New value for {0}?'.format(key))
    update_crop_in_growlog(name, key, val)


def delete_crop():
    growlog = load_growlog()
    if not growlog:
        click.echo('No growlog found')
        return
    names = [crop.name for crop in growlog]
    name = click.prompt('Which crop do you want to delete?', type=click.Choice(names))
    delete_crop_from_growlog(name)


def add():
    new_crop()
