#
# Функция получения номеров по идентификатору контакта через api сайта https://domik65.ru/
#
# Важно!!!
#
# Необходимо указывать точные (указанные на сайте) номера контактов, иначе сервер распознает
# неверные запросы и блокирует авторизацию по IP адресу на некоторое время (около часа).
#

import requests
from loguru import logger

def get_cookies(id):
    cookies = {
    }

    headers = {}

    url = 'https://domik65.ru/api/offer/' + id
    jwt = ''

    response = requests.get(url, cookies=cookies, headers=headers)

    if response.status_code == 200:
        try:
            res = response.json()
            jwt = res['data']['jwt']
            cookies = response.cookies
        except Exception as Err:
            logger.info(f'[#1] Не удалось извлечь номер контакта [{id=}] [{url=}]')
            jwt = ''
    else:
        logger.info(f'[#2] Страница отвечает ошибкой [{response.status_code=}] [{id=}] [{url=}]')
        jwt = ''

    return jwt, cookies


@logger.catch
def get_phone_number(id):
    jwt, cookies = get_cookies(str(id))

    phone_number = []

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
        'authorization': 'Bearer ' + jwt,
    }

    cookies = {
        'sakhcomid': 'qYEhRKiWdZhIm2Ye4M3VZH1wBLeIqb7NZc77vcJXw3Bt14DoGae_rJTL-9aHTQpI',
        'jwt_oauth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJzYWtoLmNvbSIsImlhdCI6MTY3ODc1NTU4NSwiZXhwIjoxNjg2NTMxNTg1LCJqdGkiOiI1NDNPZXpEOGVjbXk1WS1KeTZGTV9WTHB6LUV4U2lPejJDNWVUUkNjLUZZIiwidHlwZSI6InVzZXIiLCJyZW1lbWJlciI6dHJ1ZSwidXNlcl9pZCI6IjcxMjU1OCJ9.kRPqOgfRRJ5QhOmg9jH9zv7XkhH0f7u6FVq9DHHnoR-XmA2iwgP2j9Jx0xdtxny9',
    }

    if jwt and not jwt == '':
        url = f'https://domik65.ru/api/offer/{id}/contact'
        response = requests.get(url, cookies=cookies, headers=headers)

        if response.status_code == 200:
            try:
                res_json = response.json()
                if res_json['success'] == True:
                    phones = res_json['data']['phones']

                    for phone in phones:
                        phone_number.append(phone['number'])
            except Exception as Err:
                logger.info(f'[#3] Не удалось извлечь номер контакта [{id=}] [{url=}] [{Err=}]')
        else:
            logger.info(f'[#4] Страница отвечает ошибкой [{response.status_code=}] [{id=}] [{url=}]')
    return phone_number









