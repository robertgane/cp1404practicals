from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609


class MilesConverter(App):
    """Miles converter app"""

    message = StringProperty()

    def build(self):
        """build miles converter app"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "54.717"
        return self.root

    def handle_calculate(self):
        """handle calculation of miles to km"""
        value = self.get_valid_input()
        result = value * MILES_TO_KM
        self.message = str(result)

    def handle_increment(self, change):
        """handle increments for up and down button"""
        value = self.get_valid_input() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def get_valid_input(self):
        """get valid input, if value error, return input as 0.0"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0


MilesConverter().run()
