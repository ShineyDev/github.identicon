from typing import NamedTuple

from identicon.identicon import Identicon as Identicon


class _VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    release: str
    serial: int

version: str = ...
version_info: _VersionInfo = ...
