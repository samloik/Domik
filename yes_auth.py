import requests

cookies = {
    # '_ym_uid': '1678687847435718372',
    # '_ym_d': '1678687847',
    'sakhcomid': 'qYEhRKiWdZhIm2Ye4M3VZH1wBLeIqb7NZc77vcJXw3Bt14DoGae_rJTL-9aHTQpI',
    # '_ga': 'GA1.2.1528976573.1678687848',
    # '_gid': 'GA1.2.1862960036.1678687848',
    'jwt_oauth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJzYWtoLmNvbSIsImlhdCI6MTY3ODc1NTU4NSwiZXhwIjoxNjg2NTMxNTg1LCJqdGkiOiI1NDNPZXpEOGVjbXk1WS1KeTZGTV9WTHB6LUV4U2lPejJDNWVUUkNjLUZZIiwidHlwZSI6InVzZXIiLCJyZW1lbWJlciI6dHJ1ZSwidXNlcl9pZCI6IjcxMjU1OCJ9.kRPqOgfRRJ5QhOmg9jH9zv7XkhH0f7u6FVq9DHHnoR-XmA2iwgP2j9Jx0xdtxny9',
    # '_ym_isad': '2',
}

headers = {
    # 'authority': 'domik65.ru',
    # 'accept': 'application/json',
    # 'accept-language': 'ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJkb20tYXBpIiwiaWF0IjoxNjc4NzgxMDgzLCJleHAiOjE2Nzg4Njc0ODMsInMiOiJkb21pazY1LnJ1IiwibSI6Im9mZmVyXC80MjA1NjAiLCJxcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJwcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJicCI6ImEwM2U5Y2UxMzQwOTlkMmJkNDEwYmRjNTNlOGFiYjdkM2Y5NWMzOTcifQ.5cZeTL1LKVo0bUOu72Y7goTF_0NR9pr46kdonh2QiDVecFXxE0fKz2xMEth3G6-l',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJkb20tYXBpIiwiaWF0IjoxNjc4NzgxOTg0LCJleHAiOjE2Nzg4NjgzODQsInMiOiJkb21pazY1LnJ1IiwibSI6Im9mZmVyXC80MjA1NjAiLCJxcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJwcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJicCI6ImEwM2U5Y2UxMzQwOTlkMmJkNDEwYmRjNTNlOGFiYjdkM2Y5NWMzOTcifQ.L9Dk07kmoP3XkgEJi3elzuuZi-WM6OHapZ86CimfVfnAJxBpEsAMr58P1LeEVsjC',
    # # 'cookie': '_ym_uid=1678687847435718372; _ym_d=1678687847; sakhcomid=qYEhRKiWdZhIm2Ye4M3VZH1wBLeIqb7NZc77vcJXw3Bt14DoGae_rJTL-9aHTQpI; _ga=GA1.2.1528976573.1678687848; _gid=GA1.2.1862960036.1678687848; jwt_oauth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJzYWtoLmNvbSIsImlhdCI6MTY3ODc1NTU4NSwiZXhwIjoxNjg2NTMxNTg1LCJqdGkiOiI1NDNPZXpEOGVjbXk1WS1KeTZGTV9WTHB6LUV4U2lPejJDNWVUUkNjLUZZIiwidHlwZSI6InVzZXIiLCJyZW1lbWJlciI6dHJ1ZSwidXNlcl9pZCI6IjcxMjU1OCJ9.kRPqOgfRRJ5QhOmg9jH9zv7XkhH0f7u6FVq9DHHnoR-XmA2iwgP2j9Jx0xdtxny9; _ym_isad=2',
    # 'if-modified-since': 'Tue, 14 Mar 2023 08:02:53 GMT',
    # 'referer': 'https://domik65.ru/flat/lease/420560?search_query=e083e6ce76cd6f6db56c1f387e3d0bac',
    # 'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
    # 'sec-fetch-dest': 'empty',
    # 'sec-fetch-mode': 'cors',
    # 'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    # 'x-requested-with': 'XMLHttpRequest',
}

response = requests.get('https://domik65.ru/api/offer/420560/contact', cookies=cookies, headers=headers)
# response = requests.get('https://domik65.ru/api/offer/420560/', cookies=cookies, headers=headers)

print(response.status_code)
print(response.cookies)
print(response.text)
# print(response.json()['data']['jwt'])