class AutomationEngine:

    def process_temperature(self, temp):

        if temp > 30:
            self.turn_on_fan()

    def turn_on_fan(self):

        print("Fan turned ON automatically")