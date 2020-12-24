import requests
from key import api_key
import json


class Control(object):
    def __init__(self):
        self.url = "https://developer-api.govee.com/v1/devices"
        self.control_url = "https://developer-api.govee.com/v1/devices/control"
        self.api_key = api_key

    def get_status(self) -> requests.models.Response:
        return requests.get(self.url, headers={'Govee-API-Key': self.api_key})

    def turn_light_on(self, light: dict) -> requests.models.Response:
        value = {"device": light['device'], "model": light['model'],
                 "cmd": {"name": "turn",
                         "value": "on"}
                 }
        print(value)
        return requests.put(self.control_url, headers={'Govee-API-Key': self.api_key}, json=value)

    def turn_light_off(self, light: dict) -> requests.models.Response:
        value = {"device": light['device'], "model": light['model'],
                 "cmd": {"name": "turn",
                         "value": "off"}
                 }
        return requests.put(self.control_url, headers={'Govee-API-Key': self.api_key}, json=value)

    def set_light_colour(self, light: dict, color: str = 'blue') -> requests.models.Response:
        value = {"blue": {"device": light['device'], "model": light['model'],
                          "cmd": {"name": "color",
                                  "value": {"r": 0, "g": 0, "b": 255}
                                  }
                          }, "red": {"device": light['device'], "model": light['model'],
                                     "cmd": {"name": "color",
                                             "value": {"r": 255, "g": 0, "b": 0}
                                             }
                                     }, "green": {"device": light['device'], "model": light['model'],
                                                  "cmd": {"name": "color",
                                                          "value": {"r": 0, "g": 255, "b": 0}
                                                          }
                                                  }}
        return requests.put(self.control_url, headers={'Govee-API-Key': self.api_key}, json=value[color])

    def set_light_brightness(self, light: dict, val: int = 80) -> requests.models.Response:
        value = {"device": light['device'], "model": light['model'],
                 "cmd": {"name": "brightness",
                         "value": val
                         }
                 }
        return requests.put(self.control_url, headers={'Govee-API-Key': self.api_key}, json=value)
