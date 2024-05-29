#!/usr/bin/python3

'''
    quick doc
'''

import pickle


class CustomObject:
    '''
        quick doc
    '''

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb+") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        output = None
        with open(filename, "rb") as f:
            output = pickle.load(f)
        return output
