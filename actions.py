import datetime
import random


def choose_action(action, params):
    text = "Looking for action..."

    if action == "hello":
        person_name = params.get("given-name")
        text1 = hello(person_name)
        text2 = get_randomfact() 
        text = text1 + text2
    elif action == "time":
        text = get_time()
    elif action == "date":
        text = get_date()
    elif action == "randomfact":
        text = get_randomfact()
    elif action == "hello-language":
        foreign_language = params.get("language")
        foreign_language = foreign_language.lower()
        text = get_language(foreign_language)
    else:
        text = "No action matched!"

    return text


def get_language(foreign_language):
    """
    Tells user hello in different languages
    """
    print('language action')
    print(foreign_language)
    
    text = None
    if foreign_language == "french":
        text = "bonjour"
    elif foreign_language == "german":
        text = "hallo"
    elif foreign_language == "spanish":
        text = "hola"
    elif foreign_language == "russian":
        text = "Здравствуйте"
    elif foreign_language == "italian":
        text = "ciao"
    else:
        text = "No language found!"
    return text
        
        
def hello(person_name):
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hi " + str(person_name)
    return text


def get_time():
    """
    Tells the user the current time
    """
    print('time action')

    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    text = "The time is %d:%d:%d" % (hour, minute, second)
    return text

def get_date():
    """
    Tells the user the current date
    """
    print('date action')
    
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    year= now.year
    
    text = "The date is %d-%d-%d" % (month, day, year)
    return text

def get_randomfact():
    """
    Tells the user a random fact
    """
    print('randomfact action')
    facts= ['Banging your head against a wall burns 150 calories in an hour.', 'A flock of crows is known as a murder.', 
            'If Pinokio said "My nose will grow", it would cause a paradox.',
            'There is a 51% chance that a flipped coin will land on the side that was facing up when it was flipped.', 
            'Sunglasses make humans look more attractive because they give the illusion of a chiseled bone structure on top of a soft-featured face.', 
            'While children of identical twins are legally first cousins, genetically they are half-siblings.',
            'The man who created pop-up ads has apologized to the world for creating one of the internet\'s most hated forms of advertising.', 
            'The reason why the wedding ring is placed on the fourth finger of your left hand is because it\'s the only finger that has a vein connected directly to your heart.', 
            'The quietest room in the world is -9 decibels, quiet enough for you to hear your blood flowing.', 
            'Zerao is a stadium in Brazil in which the midfield line supposedly lies exactly on the equator, making each team defend one hemisphere.', 
            'You once held a world record when you were born for being the \'Youngest Person on The Planet\'.']
    integer=random.randint(0,10)
    
    text= "%s" % (facts[integer])
    return text
