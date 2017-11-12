import datetime
import random


def choose_action(action):
    text = "Looking for action..."

    if action == "hello":
        text = hello()
    elif action == "time":
        text = get_time()
    elif action == "date":
        text = get_date()
    elif action == "randomfact":
        text = get_randomfact()
    else:
        text = "No action matched!"

    return text


def hello():
    """
    Says "Hello World" to the user
    """
    print('hello action')

    text = "Hello World"
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
    facts= ['Banging your head against a wall burns 150 calories in an hour.', 'A flock of crows is known as a murder.', 'If Pinokio said "My nose will grow", it would cause a paradox.']
    integer=random.randint(0,2)
    
    text= "The fact is %s" % (facts[integer])
    return text
