import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"

PORT = 1883


class MQTTService:

    def __init__(self):

        self.client = mqtt.Client()

        self.client.connect(BROKER, PORT)

    def publish(self, topic, message):

        self.client.publish(topic, message)

    def subscribe(self, topic):

        self.client.subscribe(topic)