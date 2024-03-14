import time

# Define the starting point to be able to refer back to later on so that the program can be restarted by the user
def start():

    turtle_dictionary = {'donatello' : ['Mutant turtle', 'Purple mask', 'Second-in-command', 'Science and Math', 'Bo staff'], 
                     'leonardo' : ['Mutant turtle', 'Blue mask', 'First-in-command', 'Stoic discipline, Maturity, and Strategy', 'Katana'], 
                     'michelangelo' : ['Mutant turtle', 'Orange mask', 'Team Chef', 'Optimistic wit/humor and Skateboarding', 'Nunchaku'],
                     'raphael' : ['Mutant turtle', 'Red mask','Team Enforcer', 'Independent thought and Aggression', 'Sai'],
                     'splinter' : ['Mutant rat', 'Robes', 'Adoptive father and teacher', 'Wisdom, Sense of smell, and Stealth', 'Wood cane'],
                     'april' : ['Human -- Full name: April O\'Neil', 'Female-presenting clothing', 'Ally','News journalism, Computer programming, and Deductive reasoning', 'None. Skilled with various weapons'],
                     'casey' : ['Human -- Full name: Arnold Bernid "Casey" Jones', 'Ice hockey mask', 'Ally', 'Violence and Unarmed combat', 'Sports equipment']}

    print('')

    # Use the .lower() function to "sanitize" the input to account for any odd formatting
    Character = input('Type the name of one of the Teenaged Mutant Ninja Turtles, or the first name of one of their friends, and I will provide some facts about your chosen character! ').lower()

    print('')

    # Use the .capitalize() function to capitalize the first letter of the entered name
    print('Searching for information about ' + Character.capitalize() +'...')
    time.sleep(2)

    print('')

    try:
        Character_data = turtle_dictionary[Character]
        print('Name: ' + Character.capitalize())
        time.sleep(.25)
        print('Species: ' + Character_data[0])
        time.sleep(.5)
        print('Wears: ' + Character_data[1])
        time.sleep(.5)
        print('Role: ' + Character_data[2])
        time.sleep(.5)
        print('Skills: ' + Character_data[3])
        time.sleep(.5)
        print('Favorite weapon: ' + Character_data[4])
        print('')
        continueOption()

    except:
        print('Your requested character, ' + Character.capitalize() + ', was not found in our list. Sorry, but information is currently limited to the "good guy" characters who appear in the majority of comic or video media for the Teenaged Mutant Ninja Turtles franchise. Please limit your request to a single word first name (not nickname), double check your spelling, and try again.')
        print('')
        continueOption()


def continueOption():
    Optional = input('Would you like to search again? Please enter yes or no. ')
    if Optional.lower() == 'no':
        quit()
    if Optional.lower() == 'yes':
        start()
    else:
        print('Invalid response.  Please use either yes or no.')
        continueOption()


# Call the start() function to begin the program
start()
