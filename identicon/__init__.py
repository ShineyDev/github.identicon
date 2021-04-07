import collections

from identicon.identicon import Identicon


_VersionInfo = collections.namedtuple("_VersionInfo", "major minor micro releaselevel serial")

version_info = _VersionInfo(1, 0, 0, "final", 0)
version = "1.0.0"
