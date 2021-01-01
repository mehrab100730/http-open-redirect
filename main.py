import asyncio
import time
import click
import multiprocessing

from core.utils import validate_url
from core.scanner import scan

__author__  = 'Demetrius Ford'
__version__ = 'v1.0-beta'


@click.command()
@click.option('--url',
              callback=validate_url,
              required=True)
@click.option('--cookie',
              default=None)
@click.option('--workers',
              default=multiprocessing.cpu_count())
def main(url: str, cookie: str, workers: int):
    """Test for open redirect."""
    started = time.perf_counter()
    click.clear()
    click.echo(f"""
🔎 Open Redirect Scanner {{{__version__}}}
   By {__author__} (@demetriusx00)
    """)

    asyncio.run(scan(url, cookie, workers))
    elapsed = time.perf_counter() - started

    click.echo(f'🎉 completed in {elapsed:0.2f} seconds.')


if __name__ == '__main__':
    main()
