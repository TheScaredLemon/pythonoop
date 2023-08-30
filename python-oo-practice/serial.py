"""Python serial number generator."""

import random
class SerialGenerator:

    def __init__(self, start):
        self.start = start
        self.current = start
    def generate(self):
        serial_number = self.current
        self.current += 1
        return serial_number
    def reset(self):
        self.current = self.start

