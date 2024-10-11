import requests
import base
import json


class Distance:
    def __init__(self):
        self.base_city = None
        self.target_city = None

    def set_base_city(self, base_city):
        self.base_city = base_city

    def set_target_city(self, target_city):
        self.target_city = target_city

    def get_base_city(self):
        return self.base_city

    def get_target_city(self):
        return self.target_city

    def calculate_distance(self):
        try:
            url = 'https://api.codebazan.ir/distance/index.php'

            params = {
                'mabda': self.base_city,
                'maghsad': self.target_city
            }
            response = requests.get(url=url, params=params)
            if response.status_code != 200:
                return None
            return response.json()
        except Exception as e:
            return f'Exception {e}'
