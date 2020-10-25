"""Module for interaction with TopLogger."""
import json

import requests

from models import Slot


class TopLogger:

    """
    Handle communication with TopLogger REST API.
    """

    def __init__(self, user, password, gym=None):
        self.user = user
        self.password = password
        self.host = 'https://api.toplogger.nu'
        self.version = 'v1'
        self.gym = gym
        self.token = None
        self.userid = None

        self.login()

    def login(self):
        """Start session for REST API."""
        url = f'{self.host}/users/sign_in.json'

        data = {
            'user':{
                'email': self.user,
                'password': self.password
            }
        }

        response = requests.post(url, json=data)
        response.raise_for_status()

        content = response.json()
        self.token = content['authentication_token']
        self.userid = content['user_id']

    def available_slots(self, period):
        """Get available slots in given period."""
        if not self.gym:
            raise Exception('Gym cannot be None')

        slots = self._get(f"gyms/{self.gym['id']}/slots?date={period.start.date()}&"
                          f"reservation_area_id={self.gym['area_id']}&slim=true")

        available_slots = []
        # print(f"{json.dumps(slots, indent=4)}")
        for slot in slots:
            slot = Slot(slot)
            if slot.live and slot.start_time >= period.start.time() \
                    and slot.end_time <= period.end.time():
                if slot.spots > slot.spots_booked:
                    available_slots.append(slot)

        return available_slots

    def reservation_areas(self):
        """Get reservation_areas."""
        if not self.gym:
            raise Exception('Gym cannot be None')

        areas = self._get(f"gyms/{self.gym['id']}/reservation_areas")
        return areas

    def gyms(self):
        """Get all available gyms."""
        gyms = self._get('gyms.json?json_params={"includes":["gym_resources"]}')
        for gym in gyms:
            if gym["id"] == 38:
                print(json.dumps(gym, indent=2))
        return gyms

    def _get(self, path):
        response = requests.get(f"{self.host}/{self.version}/{path}")
        response.raise_for_status()

        return response.json()
