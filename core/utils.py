import urllib.parse

from click import BadParameter
from click.core import Context
from click.core import Option
from validators import url


def validate_url(ctx: Context, param: Option, value: str):
    if not url(value, public=False):
        raise BadParameter('url is not valid.')
    return value

# => Credit sqlmap-dev (@sqlmapproject)
# => https://github.com/sqlmapproject/sqlmap/blob/210a4c3a0a5dcaf984576e0597a79eb23fa9afa4/extra/vulnserver/vulnserver.py#L117-L122


def convert_cookie(cookie: str):
    if cookie is None:
        return cookie

    cookie_dict = {}
    for token in cookie.split(';'):
        token = token.strip()
        if '=' in token:
            key, value = token.split('=', 1)
            cookie_dict[key.strip()] = urllib.parse.unquote_plus(value.strip())
