import asyncio
import click

from core.utils import validate_url

__author__ = 'Demetrius Ford'


@click.command()
@click.option('--url',
              callback=validate_url,
              required=True)
@click.option('--cookie',
              default=None)
def main(url, cookie):
    """Test for open redirect."""


if __name__ == '__main__':
    main()
