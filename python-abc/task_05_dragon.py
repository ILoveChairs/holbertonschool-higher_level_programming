#!/usr/bin/python3

'''
    Fish flying
'''


class SwimMixin():
    '''
        Mixin to swim
    '''

    def swim(self):
        print("The creature swims!")


class FlyMixin():
    '''
        Mixin to fly
    '''

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    '''
        Dragon <- swim, fly
    '''

    def roar(self):
        print("The dragon roars!")
