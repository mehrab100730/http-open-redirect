import re
import urllib.parse

from typing import (Iterator,
                    Tuple,
                    TypeVar,)

from core.dorks import OPEN_REDIRECT_DORKS
from core.payloads import OPEN_REDIRECT_PAYLOADS


def make_urls(url: str) -> Iterator[Tuple[str, str]]:
    if url[-1] == '/':
        url = url[:-1]

    parsed = urllib.parse.urlsplit(url)

    if parsed.query != '':
        fuzz_params = re.findall(r'(\w+)=', parsed.query)
        for dork in OPEN_REDIRECT_DORKS:
            if dork in fuzz_params:
                for payload in OPEN_REDIRECT_PAYLOADS:
                    found = re.search(rf'{dork}=([^&]+)', url).group(1)
                    yield (url.replace(found, payload), payload)
    else:
        for payload in OPEN_REDIRECT_PAYLOADS[1:]:
            if payload[0] != '/':
                yield (f'{url}/{payload}', payload)
            else:
                yield ((url + payload), payload)
