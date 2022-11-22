from mycroft import MycroftSkill, intent_file_handler
import random

class NumberPicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('picker.number.intent')
    def handle_picker_number(self, message):
        number1 = int(message.data.get('number1'))
        number2 = int(message.data.get('number2'))
        
        self.speak_dialog('picker.number', data={
            'number' : random.randint(number1,number2)
        })
        
        


def create_skill():
    return NumberPicker()

