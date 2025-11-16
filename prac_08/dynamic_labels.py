from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Kivy App to dynamically add labels."""
    def __init__(self, **kwargs):
        """Initialize the list of names."""
        super().__init__(**kwargs)
        self.names = ["Bob", "Joe", "Alice", "George", "John"]

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create the labels from list and dynamically add them."""
        for name in self.names:
            dynamic_label = Label(text=name)
            self.root.ids.main.add_widget(dynamic_label)


DynamicLabelsApp().run()
