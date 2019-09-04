#!/usr/bin/env python3
from typing import List

class Person(object):

    name: str = ""
    liked_people: List[str] = []
    def __init__(self, name: str=""):
        self.name = name
    
    def likes(self,person:object):
        self.liked_people.append(person.name)

bob = Person("Bob")
alice = Person("Alice")

bob.likes(alice)

print(bob.liked_people)