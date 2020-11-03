"""All class types used in this script."""
from __future__ import annotations

from datetime import datetime

from dataclasses import dataclass
from dataclasses import field
from dataclasses_json import config
from dataclasses_json import dataclass_json
from dataclasses_json import Undefined
from dateutil.parser import parse
from dateutil.tz import gettz


@dataclass
class Period:
    """
    Object for holding period data.

    A period has a start and an end date, that's all.
    """
    start: datetime
    end: datetime

    @classmethod
    def from_strings(cls, start: str, end: str) -> Period:
        """Create instance of Period from to 'date' strings.

        The start and end strings are converted to datetime objects by dateutil.parser.parse
        """
        tzinfo = gettz()
        return cls(parse(start).replace(tzinfo=tzinfo), parse(end).replace(tzinfo=tzinfo))

    def __str__(self):
        """String representations of this dataclass"""
        return f"Start: {self.start}, End: {self.end}"


@dataclass
class QueueItem:
    """
    Dataclass for queued items, an item represents a period which need to be checked.

    An item consists of a gym and a period. The property handled is set when a notification is sent
    for an available slot.
    """
    gym: dict
    period: Period
    handled: bool = False

    def __str__(self):
        """String representations of this dataclass"""
        notified = ' NOTIFIED' if self.handled else ''
        return f"{self.gym['name']}  ->  {self.period.start.date().strftime('%a %d %b')} " \
               f"{self.period.start.strftime('%H:%M')} - {self.period.end.strftime('%H:%M')}" \
               f"{notified}"

    def set_handled(self, handled):
        """Set handled property."""
        self.handled = handled


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Gym:
    """
    Dataclass for TopLogger gym.

    Only a few properties are saved others aren't needed for this script.
    """
    id: int
    name: str
    slug: str


@dataclass_json
@dataclass
class ReservationArea:
    """
    Dataclass for TopLogger Reservation Area for a gym.

    Not all gyms have reservation area(s).
    """
    id: int
    name: str
    capacity: int


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Slot:
    """
    Dataclass for Toplogger slot.

    Only a few properties are saved others aren't needed for this script.
    """
    id: int
    start_at: datetime = field(metadata=config(encoder=datetime.isoformat, decoder=parse))
    end_at: datetime = field(metadata=config(encoder=datetime.isoformat, decoder=parse))
    spots: int
    spots_booked: int

    @property
    def date(self) -> datetime:
        """The date of this slot, based on the start datetime."""
        return self.start_at.date()

    @property
    def spots_available(self) -> int:
        """Calculate how many spots are available for this slot."""
        return self.spots - self.spots_booked
