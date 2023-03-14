# пример применения


from domik import get_phone_number


def test():

    contacts = ['709088', '584930', '420560', '713567', '199781', '717797']


    for contact in contacts:
        print(f'Контакт: [{contact}] тел: {get_phone_number(contact)}')


import random
from time_decorator import *
@timeit
def test2():

    contacts = ['709088', '584930', '420560', '713567', '199781', '717797']

    i=0
    while True:
        contact = random.choice(contacts)
        print(f'[{i:5}] Контакт: [{contact}] тел: {get_phone_number(contact)}')
        i += 1


if __name__ == '__main__':
    test2()

