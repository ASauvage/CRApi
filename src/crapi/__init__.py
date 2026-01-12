#  .d8888b.  8888888b.         d8888          d8b 
# d88P  Y88b 888   Y88b       d88888          Y8P 
# 888    888 888    888      d88P888              
# 888        888   d88P     d88P 888 88888b.  888 
# 888        8888888P"     d88P  888 888 "88b 888 
# 888    888 888 T88b     d88P   888 888  888 888 
# Y88b  d88P 888  T88b   d8888888888 888 d88P 888 
#  "Y8888P"  888   T88b d88P     888 88888P"  888 
#                                    888          
#                                    888          
#                                    888         

"""
crapi
~~~~~~~~~~~~~~

Usage::
    >>> from crapi import CRApiClient
    >>> client = CRApiClient("<API TOKEN>")
    >>> player = client.players.get_by_tag("#2PCRVJUYQ")
"""


MAJOR_VERSION = '1'
MINOR_VERSION = '0'
PATCH_VERSION = '0'

__version__ = '.'.join((MAJOR_VERSION, MINOR_VERSION, PATCH_VERSION))
__all__ = [
    "CRApiClient"
]

from .client import CRApiClient
