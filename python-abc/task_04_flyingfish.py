#!/usr/bin/python3

'''
    Fish flying
'''


class Fish():
    '''
        Fish
    '''

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird():
    '''
        Bird
    '''

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    '''
        FlyingFish
    '''

    def swim(self):
        print("The flying fish is swimming")

    def fly(self):
        print("The flying fish is flying")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
