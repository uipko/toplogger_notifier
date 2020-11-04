"""Module for interaction with TopLogger."""
import logging
from typing import Optional
from typing import List
from typing import Dict

import requests

from models import Period
from models import ReservationArea
from models import Slot


class TopLogger:

    """
    Handle communication with TopLogger REST API.
    """

    def __init__(self, user: Optional[str] = None, password: Optional[str] = None,
                 gym: Optional[Dict[str, any]] = None):
        self.user = user
        self.password = password
        self.host = 'https://api.toplogger.nu'
        self.version = 'v1'
        self.gym = gym
        self.token = None
        self.userid = None

    def login(self):
        """Start session for REST API."""
        url = f'{self.host}/users/sign_in.json'
        data = {
            'user': {
                'email': self.user,
                'password': self.password
            }
        }
        response = requests.post(url, json=data)
        response.raise_for_status()
        content = response.json()
        self.token = content['authentication_token']
        self.userid = content['user_id']

    def available_slots(self, period: Period) -> List[Slot]:
        """Get available slots in given period."""
        if not self.gym:
            raise Exception('Gym cannot be None')

        slots = self._get(f"gyms/{self.gym['id']}/slots?date={period.start.date()}&"
                          f"reservation_area_id={self.gym['area_id']}")
        available_slots = []
        for slot in slots:
            slot = Slot.from_dict(slot)  # pylint: disable=maybe-no-member
            if (slot.start_at >= period.start and slot.end_at <= period.end
                    and slot.spots > slot.spots_booked):
                available_slots.append(slot)
        return available_slots

    def reservation_areas(self) -> ReservationArea:
        """Get reservation_areas."""
        if not self.gym:
            raise Exception('Gym cannot be None')
        areas = self._get(f"gyms/{self.gym['id']}/reservation_areas")
        return areas

    def gyms(self):
        """Get all available gyms."""
        gyms = self._get('gyms')
        return gyms

    def _get(self, path):
        url = f"{self.host}/{self.version}/{path}"
        logging.info(f'Call: {url}')
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
