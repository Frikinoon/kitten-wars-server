from enum import Enum

def is_message(msg):
    return isinstance(msg, dict) and Message.key_message in msg

__message_types_string = 'ERROR JOIN_GAME LEAVE_GAME START_GAME GAME_STATE'
__message_types_list = __message_types_string.split(sep=' ')
MessageType = Enum('MessageType', __message_types_string)

class Message():
    def __init__(self, msg_type, msg_body):
        self.type = msg_type
        self.body = msg_body

class UnintelligibleMessage(Message):
    def __init__(self):
        super().__init__(MessageType.ERROR, {})