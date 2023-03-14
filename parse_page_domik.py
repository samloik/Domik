# пример применение


from domik import get_phone_number


def test():

    list_contacts = ['709088', '584930', '420560', '713567']

    for contact in list_contacts:
        print(get_phone_number(contact))


if __name__ == '__main__':
    test()