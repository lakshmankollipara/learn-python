## Custom module used in Tutorial2

import sys
import time

__version__ = "1.0.0"

class MyClass():
    '''This is my own created python module 
    which prints line in given number of times
    used in Tutotrial 2'''  ## Documentation
    _msg = "This a message from my Custom Module"

    def __init__(self, msg, n):
        self._msg = msg
        self._n = n

    def get_msg(self):
        return self._msg

    def n_times(self):
        for i in range(0, self._n):
            print(self.get_msg())
