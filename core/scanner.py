import click
import pypeln as pl
import urllib.parse

from aiohttp import ClientSession
from aiohttp import TCPConnector

from core.urls import create_urls
from core.utils import convert_cookie

# => Target redirect

HACKER_ONE = 'https://www.hackerone.com'

# => Known redirects

HTTP_CODES = (301,
              302,
              303,
              307,
              308)


async def scan(url: str, cookie: str, workers: int):
    async with ClientSession(connector=TCPConnector(limit=0),
                             cookies=convert_cookie(cookie)) as session:
        async def analyze_redirect(url):
            async with session.get(url, allow_redirects=True) as response:
                redirected = any(redirect.status in HTTP_CODES for
                                 redirect in response.history)
                vulnerable = redirected and \
                    response.url.human_repr() == HACKER_ONE
                if vulnerable:
                    click.echo(f'😈 {urllib.parse.unquote_plus(url)}')
        await pl.task.each(analyze_redirect,
                           create_urls(url),
                           workers=workers)
