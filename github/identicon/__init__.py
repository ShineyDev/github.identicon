import collections

from identicon.identicon import Identicon


__all__ = [
    "Identicon",
]


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro release serial")

version = "1.0.0"
version_info = _VersionInfo(1, 0, 0, "final", 0)
