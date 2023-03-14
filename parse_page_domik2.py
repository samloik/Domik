# пример применения


from domik import get_phone_number

from bs4 import BeautifulSoup
from loguru import logger

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


def get_contacts():
    cookies = {}
    headers = {}

    res = ''

    url = 'https://domik65.ru/flat/lease?page='

    for i in range(50):
        response = requests.get(url, cookies=cookies, headers=headers)

        if response.status_code == 200:
            try:
                res = response.text
                cookies = response.cookies
            except Exception as Err:
                logger.info(f'[#1] Не удалось извлечь номер контакта [{id=}] [{url=}]')
                exit(1)

        else:
            logger.info(f'[#2] Страница отвечает ошибкой [{response.status_code=}] [{id=}] [{url=}]')
            exit(1)

    # if
    # soup = BeautifulSoup(response, 'lxml')

    # bs_all_products = soup.find_all(class_='phytpj4_plp largeCard')





if __name__ == '__main__':
    get_contacts()

