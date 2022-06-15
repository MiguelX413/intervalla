from typing import Iterable, List, Optional, Sequence, Tuple

__version__: str

def match_indices(string: str, substring: str) -> List[int]:
    """Returns a list of the UTF-8 indices of disjoint matches, from start to end."""

def match_utf16_indices(string: str, substring: str) -> List[int]:
    """Returns a list of the UTF-16 indices of disjoint matches, from start to end."""

def match_byte_indices(string: str, substring: str) -> List[int]:
    """Returns a list of the byte indices of disjoint matches, from start to end."""

def rmatch_indices(string: str, substring: str) -> List[int]:
    """Returns a list of the UTF-8 indices of disjoint matches, from end to start."""

def rmatch_utf16_indices(string: str, substring: str) -> List[int]:
    """Returns a list of the UTF-16 indices of disjoint matches, from end to start."""

def rmatch_byte_indices(string: str, substring: str) -> List[int]:
    """Returns a list of the byte indices of disjoint matches, from end to start."""

def utf16len(string: str) -> int:
    """A function that returns the UTF-16 length of a string."""

class Interval:
    """A class used to represent intervals."""

    def __init__(
        self, interval_list: Optional[Sequence[Tuple[int, int]]] = ...
    ) -> None: ...
    def union(self, *other: Iterable[Interval]) -> Interval: ...
    def union_update(self, *other: Iterable[Interval]) -> None: ...
    def __contains__(self, item: int) -> bool: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __or__(self, other: Interval) -> Interval: ...
    def __ior__(self, other: Interval) -> None: ...
