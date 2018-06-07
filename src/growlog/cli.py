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
import click


@click.command()
@click.option('--title', prompt='Your site\'s title',
              help='The name of your site.')
@click.option('--description', prompt='Your site\'s description',
              help='A short description of your site.')
@click.option('--baseurl', default='http://localhost:1313',
              help='The base url of your site.')
def main(title, description, baseurl):
    click.echo('Retrieving your growlog')


@click.command()
@click.argument('names', nargs=-1)
def main(names):
    click.echo(repr(names))
