#
#
#
#
# 
#

"""
crapi
~~~~~~~~~~~~~~

Usage::
    >>> from crapi import CRApiClient
    >>> client = CRApiClient("<API TOKEN>")
    >>> player = client.players.get_by_tag("#TAG")
"""


MAJOR_VERSION = '1'
MINOR_VERSION = '0'
PATCH_VERSION = '0'

__version__ = '.'.join((MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION))
__all__ = [
    "CRApiClient"
]

from .client import CRApiClient
