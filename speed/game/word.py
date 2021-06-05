import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word(Actor):
    """The word that the player must type to score points. 
    
    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the Word is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, set's the 
        text and moves the food to a random position within the boundary of the 
        screen.
        
        Args:
            self (Actor): an instance of Actor.
        """
        super().__init__()
        self._points = 0
        self.set_text("@")
        self.reset()
    
    def get_points(self):
        """Gets the points this Word is worth.
        
        Args:
            self (Word): an instance of Word.

        Returns:
            integer: The points this Word is worth.
        """
        return self._points

    def Next_word(self):
        """Resets the word bycalling a new one from the list and sending it down the screen.
        
        Args:
            self (Word): an instance of Word.
        """
        self._points = random.randint(1, 5)
        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)
        
