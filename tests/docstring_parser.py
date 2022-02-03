"""
参照URL
https://blog.tamaosa.com/2021/pytest-html-specification/
"""
import re
from typing import List, Tuple, Dict
from itertools import takewhile


_section_rgx = re.compile(r"^\s*[a-zA-Z]+:\s*$")
_lspace_rgx = re.compile(r"^\s*")


def _parse_section(lines: List[str]) -> List[Tuple[int, str]]:
    matches = map(lambda x: _section_rgx.match(x), lines)
    indexes = [i for i, x in enumerate(matches) if x is not None]
    return list(map(lambda x: (x, lines[x].strip()[:-1]), indexes))


def _count_lspace(s: str) -> int:
    rgx = _lspace_rgx.match(s)
    if rgx is not None:
        return rgx.end()
    return 0


def _parse_content(index: int, lines: List[str]) -> str:
    lspace = _count_lspace(lines[index])
    i = index + 1
    contents = takewhile(lambda x: _count_lspace(x) > lspace, lines[i:])
    return "".join(map(lambda x: x.strip(), contents))


def parse(docstring: str) -> Dict[str, str]:
    """🚧sloppy docstring parser🚧"""
    lines = docstring.splitlines()
    sections = _parse_section(lines)
    return dict(map(lambda x: (x[1], _parse_content(x[0], lines)), sections))