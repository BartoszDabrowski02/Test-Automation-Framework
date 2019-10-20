import random


def create_unique_email():
    unique_email = generate_unique_word() + '_' + generate_unique_id() + '@' + generate_email_domain()
    print(unique_email)
    return unique_email

def generate_unique_word():
    """This function generate random word"""
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    word_length = random.randint(3, 8)
    word = ''
    for i in range(word_length):
        if i == 0:
            word += random.choice(LETTERS).upper()
        else:
            word += random.choice(LETTERS)
    return word

def generate_unique_id():
    return str(random.randint(1000, 9999))

def generate_email_domain():
    values = {
        'first_part' : ['aol', 'bartosz', 'gmail', 'company', 'strange-test'],
        'second_part' : ['pl', 'com']
    }
    email_domain = random.choice(values['first_part']) + '.' + random.choice(values['second_part'])
    return email_domain
