"""
All class types used in this script.
"""
from dateutil.parser import parse


class QueueItem:
    """
    Class for holding Item data used for queueing checks for a slot.
    """

    def __init__(self, gym, period, handled=False):
        self.gym = gym
        self.period = period
        self.handled = handled

    def __str__(self):
        notified = ' NOTIFIED' if self.handled else ''
        return f"{self.gym['name']}  ::  {self.period.start.date()} " \
               f"{self.period.start.strftime('%H:%M')} - {self.period.end.strftime('%H:%M')}" \
               f"{notified }"

    def set_handled(self, handled):
        """
        Set handled property.
        """
        self.handled = handled


class Period:
    """
    Object for holding period data.
    """

    def __init__(self, start, end):
        self.start = parse(start)
        self.end = parse(end)

    def __str__(self):
        return f"Start: {self.start}, End: {self.end}"


class Gym:
    """
    Class for holding data of a TopLogger gym.

    A JSON slot looks like this:
    {
    "id": 38,
    "id_name": "delfts_bleau",
    "slug": "delfts-bleau",
    "name": "Delfts Bleau",
    "name_short": "Delfts Bleau",
    "live": true,
    "latitude": "51.9946241",
    "longitude": "4.3675542",
    "address": "Schieweg 15",
    "city": "Delft",
    "postal_code": "2627 AN",
    "country": "NL",
    "url_website": "https://www.delftsbleau.nl/",
    "url_facebook": "https://www.facebook.com/DelftsBleau",
    "phone_number": "+31 15 7600090",
    "nr_of_climbs": 174,
    "nr_of_routes": 0,
    "nr_of_boulders": 174,
    "my_ascends_count": 0,
    "local_device_pwd": "ea51ac65ccc9f3e2ed3037ed8132f3f8b15bc612",
    "serializer": "list",
    "scale_collapse_climbs": "0.4",
    "scale_collapse_walls": "0.1",
    "gym_resources": []
    }
    """

    def __init__(self, gym):
        """
        Initialize object based on JSON slot object.
        """
        self.id = gym['id']
        self.name = gym["id_name"]
        self.slug = gym["slug"]
        self.name = gym["name"]
        self.name_short = gym["name_short"]


class ReservationArea:
    """
    {
        "id": 31,
        "name": "Bouldering",
        "capacity": 72
    }
    """

    def __init__(self, area):
        """
        Initialize object based on JSON reservation_area object.
        """
        self.id = area['id']
        self.name = area['name']
        self.capacity = area['capacity']


class Slot:
    """
    Class for holding data of a Toplogger slot.

    A JSON slot looks like this:
    {
        "id": 92119,
        "reservation_area_id": 31,
        "start_at": "2020-10-12T16:30:00.000+02:00",
        "end_at": "2020-10-12T18:30:00.000+02:00",
        "checkinend_at": "2020-10-12T16:45:00.000+02:00",
        "spots": 16,
        "spots_booked": 8,
        "details": null,
        "live": true
    }
    """

    def __init__(self, slot):
        """
        Initialize object based on JSON slot object.
        """
        start_at = parse(slot['start_at'])
        end_at = parse(slot['end_at'])
        self.id = slot['id']
        self.spots = slot['spots']
        self.spots_booked = slot['spots_booked']
        self.live = slot['live']
        self.date = start_at.date()
        self.start_time = start_at.time()
        self.end_time = end_at.time()

    @property
    def spots_available(self):
        """
        Calculate how many spots are available for this slot.
        """
        return self.spots - self.spots_booked
