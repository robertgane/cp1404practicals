from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create buttons from a dictionary"""
        for name in self.name_to_phone:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetsApp().run()
