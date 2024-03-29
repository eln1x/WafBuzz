# Copyright (C) AB Strakt
# See LICENSE for details.

"""
pyOpenSSL - A simple wrapper around the OpenSSL library
"""

from core.libs.thirdparty.OpenSSL import crypto, SSL
from core.libs.thirdparty.OpenSSL.version import (
    __author__, __copyright__, __email__, __license__, __summary__, __title__,
    __uri__, __version__,
)


__all__ = [
    "SSL", "crypto",

    "__author__", "__copyright__", "__email__", "__license__", "__summary__",
    "__title__", "__uri__", "__version__",
]
