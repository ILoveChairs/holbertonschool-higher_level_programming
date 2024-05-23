#!/usr/bin/python3

'''
    Using ABC
'''

from abc import ABC, abstractmethod


class Animal(ABC):
    '''
        Animal
    '''

    
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''
        Dog
    '''

    def sound(self):
        return "Bark"


class Cat(Animal):
    '''
        Cat
    '''

    def sound(self):
        return "Meow"
