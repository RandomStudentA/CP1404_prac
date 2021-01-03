from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name_list = {"Name", "Name", "Name", "Name", "Name", "Name"}

    def build(self):
        self.title = "Dynamic Lables"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        for name in self.name_list:
            temp_button = Button(text=name, id=name)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_labels(temp_button)

    def press_entry(self, instance):

        name = instance.id
        self.status_text = "Name is {}".format(name, self.name_list[name])

    def clear_all(self):
        self.root.ids.entries_box.clear_labels()


DynamicLabelsApp().run()