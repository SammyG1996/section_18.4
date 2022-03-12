"""Word Finder: finds random words from a dictionary."""
import random

"""
This class will allow you to start pass in a file 
path to a word document and then retreive a random word 
from the list
"""
class WordFinder:
    ...
    def __init__(self, file_path):
        self.file_path = file_path

    """
    This function will do the healvy lifting of actually creating the list. 
    It also removes the "/n" from the line. It returns a list containing all
    the words from each line.  
    """
    def get_words(self):
        file = open(self.file_path, 'r')
        lst = []
        for line in file: 
            lst.append(line.strip())
        return lst 

    """
    this will take the list from get_words and selct a ramdom word using 
    the random.randrange method to get a random number and return the the
    contained at that index number
    """
    def random(self): 
        lst = self.get_words()
        rand = random.randrange(0, len(lst))
        return lst[rand]


"""
This class is very simmilar to the WordFinder class and inherits from it. However
it has the ability to filter the list so it does not contain the headings or 
empty strings.
"""
class SpecialWordFinder(WordFinder):
    ...
    def __init_subclass__(self, file_path):
        super().__init__(file_path)

    """
    This function takes the list returned from the original get_words() function 
    but it filters using a list comprehension to remove any string that contains
    the char # (since this marks the headers) and any empty strings.
    
    """
    def get_words(self):
        lst = super().get_words()
        return [item for item in lst if item.find('#') == -1 and item != '']
