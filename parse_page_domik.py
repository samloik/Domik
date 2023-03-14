# пример применения


from domik import get_phone_number


def test():

    contacts = ['709088', '584930', '420560', '713567', '199781', '717797']

    for contact in contacts:
        print(f'Контакт: [{contact}] тел: [{get_phone_number(contact)}]')


if __name__ == '__main__':
    test()