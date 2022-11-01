from mycroft import MycroftSkill, intent_file_handler


class NumberPicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('picker.number.intent')
    def handle_picker_number(self, message):
        self.speak_dialog('picker.number')


def create_skill():
    return NumberPicker()

