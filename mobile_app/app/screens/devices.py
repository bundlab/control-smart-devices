from kivy.uix.screenmanager import Screen
from services.mqtt_service import MQTTService


class DevicesScreen(Screen):

    mqtt = MQTTService()

    def light_on(self):
        self.mqtt.publish("home/light", "ON")

    def light_off(self):
        self.mqtt.publish("home/light", "OFF")

    def fan_on(self):
        self.mqtt.publish("home/fan", "ON")

    def fan_off(self):
        self.mqtt.publish("home/fan", "OFF")