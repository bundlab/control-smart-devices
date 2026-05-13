from kivy.uix.screenmanager import Screen
from kivymd.toast import toast


class AutomationScreen(Screen):

    def create_rule(self):

        rule = {
            "sensor": "temperature",
            "condition": ">",
            "value": 30,
            "action": "turn_on_fan"
        }

        print(rule)
        toast("Automation Rule Created")