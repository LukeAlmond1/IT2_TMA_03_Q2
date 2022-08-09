# 22D TMA03 Q2
"""
This flashcard program allows the user to ask for a glossary entry. In response the program randomly picks an entry from all the glossary entries. It then initialises both word & definition variables to the corresponding properties on that entry. The decision to prompt the user for the definition or the entry is decided using the flip of a coin model to randomly set the variable to_show to either heads or tails. Based off of this the user will then be either shown the definition or the word. The user can repeatedly ask for an entry and also has the option to quit the program instead of seeing another entry
"""

from random import *

# *** Modify the body of the show_flashcard function so that it
# implements yout algorithm from part i. Also modify the docstring
# for the program and the docstring for the function, to take
# account of the changes and their effect. ***


def show_flashcard():
    """ 
      Randomly decide whether to ask for the definition or the entry.
      When the user then clicks return show either the definition or the         word based on the randomly determined value of to_show
    """
    # RANDOMISE TO_SHOW VARIABLE
    to_show = choice(list(['heads', 'tails']))

    # CHOOSE RANDOM ENTRY FROM GLOSSARY
    word = choice(list(glossary))
    definition = glossary[word]

    # PRINT QUESTION & HANDLE RESPONSE
    if to_show == 'heads':
        print("What is the definition for this entry " + word)
        input('Press return to see the entry')
        print(definition)

    if to_show == 'tails':
        print("What is the entry for the definition " + definition)
        input('Press return to see the entry')
        print(word)


# Set up the glossary

glossary = {
    'word1': 'definition1',
    'word2': 'definition2',
    'word3': 'definition3'
}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')
