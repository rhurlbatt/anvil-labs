# SPDX-License-Identifier: MIT
# Copyright (c) 2021 anvilistas

from ..cluegen import DatumBase, cluegen

_version__ = "0.0.1"


def enum(name, members):
    return type(name, (), {member: member for member in members})


def all_slots(cls):
    slots = []
    for cls in cls.__mro__:
        slots[0:0] = getattr(cls, "__slots__", [])
    return slots


class Slotum(DatumBase):
    __slots__ = ()

    @classmethod
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.__match_args__ = tuple(all_slots(cls))

    @cluegen
    def __init__(cls):
        slots = all_slots(cls)
        return (
            "def __init__(self, "
            + ",".join(slots)
            + "):\n"
            + "\n".join(f"    self.{name} = {name}" for name in slots)
        )

    @cluegen
    def __repr__(cls):
        slots = all_slots(cls)
        return (
            "def __repr__(self):\n"
            + f'    return f"{cls.__name__}('
            + ", ".join("%s={self.%s!r}" % (name, name) for name in slots)
            + ')"'
        )
