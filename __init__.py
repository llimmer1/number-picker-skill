from mycroft import MycroftSkill, intent_file_handler
import random

class NumberPicker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    @intent_file_handler('picker.number.intent')
    def initialize(self):
        self.register_intent_file('picker.number.intent', self.handle_picker_number)
        self.register_entity_file('number1.entity')
        self.register_entity_file('number2.entity')

    def handle_picker_number(self, message):
        self.log.info(message)
        number1 = int(message.data.get('number1'))
        number2 = int(message.data.get('number2'))
        
        self.speak_dialog('picker.number', data={
            'number' : random.randint(number1,number2)
        })
        
        


def create_skill():
    return NumberPicker()

