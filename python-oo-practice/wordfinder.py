"""Word Finder: finds random words from a dictionary."""

import random
class WordFinder:
    
    def __init__(self, filepath):
        with open(filepath, 'r') as file:
            self.words = [line.strip() for line in file if line.strip()]
        print(f"{len(self.words)} words read")
    
    def random(self):
        return random.choice(self.words)
    
    class SpecialWordFinder(WordFinder):
    
    def __init__(self, filepath):
        super().__init__(filepath)
    
    def random(self):
        valid_words = [word for word in self.words if not word.startswith('#')]
        return random.choice(valid_words)