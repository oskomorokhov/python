#!/usr/bin/env checkio --domain=py run dialogues

# https://py.checkio.org/mission/dialogues/

# The modern world is filled with means of communication - the social networks, messengers, phone calls, SMS etc.But sometimes in every communication channel a flaw can be detected and in the moments like that you think to yourself: "I should create my own messenger which won’t have problems like this one".
# In this mission you’ll get your chance.
# Your task is to create a Chat class which could help a Human(name) and Robot(serial_number) to make a conversation. This class should have a few methods:
# connect_human()- connects human to the chat.
# connect_robot()- connects robot to the chat.
# show_human_dialogue()- shows the dialog as the human sees it - as simple text.
# show_robot_dialogue()- shows the dialog as the robot perceives it - as the set of ones and zeroes. To simplify the task, just replace every vowel ('aeiouAEIOU') with "0", and the rest symbols (consonants, white spaces and special signs like ",", "!", etc.) with "1".
# Dialog for the human should be displayed like this:
# (human name) said: message text
# (robot serial number): message text
# For the robot:
# (human name) said: 11100100011
# (robot serial number) said: 100011100101
# Interlocutors should have asend()method for sending messages to the dialog.
# In this mission you could use theMediatordesign pattern.
#
# Example:
# chat = Chat()
# karl = Human("Karl")
# bot = Robot("R2D2")
# chat.connect_human(karl)
# chat.connect_robot(bot)
# karl.send("Hi! What's new?")
# bot.send("Hello, human. Could we speak later about it?")
# chat.show_human_dialogue() == """Karl said: Hi! What's new?
# R2D2 said: Hello, human. Could we speak later about it?"""
# chat.show_robot_dialogue() == """Karl said: 101111011111011
# R2D2 said: 10110111010111100111101110011101011010011011"""
#
#
#
# Input:Interlocutors and the text of messages.
#
# Output:A dialog (the multiline string).
#
# Precondition:2 interlocutors.
#
#
# END_DESC

from datetime import datetime
from datetime import timedelta

VOWELS = "aeiou"


class Chat:

    def __init__(self):
        self.dialogue = ""

    def connect_human(self, human):
        self.human = human

    def connect_robot(self, robot):
        self.robot = robot

    def show_human_dialogue(self):
        self.human_msg, self.robot_msg = self.human.msg, self.robot.msg
        self.human_msg = [[x, self.human.name+' said: ' + y]
                          for x, y in self.human_msg]
        self.robot_msg = [[x, self.robot.name+' said: ' + y]
                          for x, y in self.robot_msg]
        self.dialogue = sorted(
            self.human_msg+self.robot_msg, key=lambda x: x[0])
        self.dialogue = '\n'.join([x[1] for x in self.dialogue])
        return self.dialogue

    def show_robot_dialogue(self):
        self.human_msg, self.robot_msg = self.human.msg, self.robot.msg
        self.human_msg = [[x, self.human.name+' said: ' + ''.join(
            ["0" if i in VOWELS else "1" for i in y])] for x, y in self.human_msg]
        self.robot_msg = [[x, self.robot.name+' said: ' + ''.join(
            ["0" if i in VOWELS else "1" for i in y])] for x, y in self.robot_msg]
        self.dialogue = sorted(
            self.human_msg+self.robot_msg, key=lambda x: x[0])
        self.dialogue = '\n'.join([x[1] for x in self.dialogue])
        return self.dialogue


class Human:
    def __init__(self, name=None):
        self.name = name
        self.msg = []

    def send(self, text=""):
        self.msg.append([datetime.now(), text])


class Robot:
    def __init__(self, name=None):
        self.name = name
        self.msg = []

    def send(self, text=""):
        self.msg.append([datetime.now(), text])


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chat = Chat()
    karl = Human("Karl")
    bot = Robot("R2D2")
    chat.connect_human(karl)
    chat.connect_robot(bot)
    chat.show_human_dialogue()
    chat.show_robot_dialogue()

    '''assert chat.show_human_dialogue() == """Karl said: Hi! What's new?
R2D2 said: Hello, human. Could we speak later about it?"""
    assert chat.show_robot_dialogue() == """Karl said: 101111011111011
R2D2 said: 10110111010111100111101110011101011010011011"""'''

    print("Coding complete? Let's try tests!")
