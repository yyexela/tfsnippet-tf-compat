"""
This package provides shortcuts to utilities from second-level packages.
"""

from tfsnippet.utils.reuse import *

__all__ = [
    'get_reuse_stack_top', 'instance_reuse', 'global_reuse',
    'VarScopeObject'
]
