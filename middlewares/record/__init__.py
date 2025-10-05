from .direct import parse_message as parse_direct_message
from .indirect import parse_message as parse_indirect_message


__all__ = [
    "parse_direct_message",
    "parse_indirect_message",
]