import requests

# cookies = {
#     '_ym_uid': '1678690320442019797',
#     '_ym_d': '1678690320',
#     '_ga': 'GA1.2.774751908.1678690320',
#     '_gid': 'GA1.2.529367907.1678690320',
#     'sakhcomid': 'Bt41XkoUc9YvwPxcvSMR_Ld7ScGDfr7wkpNwGuffL1e3lnN1dvCZtSAnW9mYuIEH',
#     '_ym_isad': '2',
#     'jwt_oauth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJzYWtoLmNvbSIsImlhdCI6MTY3ODc3OTUzMiwiZXhwIjoxNjc4NzgzMTMyLCJqdGkiOiJ2NUF2RVJMYWFsdU5DY1ZkTEZ5aTE5eFl6R20tNVBPckk1STVrX05WZXdzIiwidHlwZSI6Imd1ZXN0In0.M2FJY-Ep6Xc51ngDVEzBohKN2hLyiGeVwf6rNBFGAJYphLcRDgxJ-0ekbpYef_H6',
# }

cookies = {
    'sakhcomid': 'qYEhRKiWdZhIm2Ye4M3VZH1wBLeIqb7NZc77vcJXw3Bt14DoGae_rJTL-9aHTQpI',
    'jwt_oauth': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJzYWtoLmNvbSIsImlhdCI6MTY3ODc1NTU4NSwiZXhwIjoxNjg2NTMxNTg1LCJqdGkiOiI1NDNPZXpEOGVjbXk1WS1KeTZGTV9WTHB6LUV4U2lPejJDNWVUUkNjLUZZIiwidHlwZSI6InVzZXIiLCJyZW1lbWJlciI6dHJ1ZSwidXNlcl9pZCI6IjcxMjU1OCJ9.kRPqOgfRRJ5QhOmg9jH9zv7XkhH0f7u6FVq9DHHnoR-XmA2iwgP2j9Jx0xdtxny9',
}

headers = {
    # 'authority': 'domik65.ru',
    # 'accept': 'application/json',
    # 'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJkb20tYXBpIiwiaWF0IjoxNjc4NjkwMzA5LCJleHAiOjE2Nzg3NzY3MDksInMiOiJkb21pazY1LnJ1IiwibSI6Im9mZmVyXC80MjA1NjAiLCJxcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJwcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJicCI6ImEwM2U5Y2UxMzQwOTlkMmJkNDEwYmRjNTNlOGFiYjdkM2Y5NWMzOTcifQ.nI8PSW7VWXeOlOkBcdC8n0BYE9Nq-cz-zvtRga5RBvtW81Fn7EeP6xma9GDT_rsC',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJkb20tYXBpIiwiaWF0IjoxNjc4NzgyMTAzLCJleHAiOjE2Nzg4Njg1MDMsInMiOiJkb21pazY1LnJ1IiwibSI6Im9mZmVyXC80MjA1NjAiLCJxcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJwcCI6Ijg3Mzk2MDI1NTRjN2YzMjQxOTU4ZTNjYzliNTdmZGVjYjQ3NGQ1MDgiLCJicCI6ImEwM2U5Y2UxMzQwOTlkMmJkNDEwYmRjNTNlOGFiYjdkM2Y5NWMzOTcifQ.zaSgQMk2oVD7zFLhcuDaPzjcgte6oa1gKxX1TIobUhWYJ7pijOoNF5akGCI9ggpy',
    # 'cookie': '_ym_uid=1678690320442019797; _ym_d=1678690320; _ga=GA1.2.774751908.1678690320; _gid=GA1.2.529367907.1678690320; sakhcomid=Bt41XkoUc9YvwPxcvSMR_Ld7ScGDfr7wkpNwGuffL1e3lnN1dvCZtSAnW9mYuIEH; _ym_isad=2; jwt_oauth=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzM4NCJ9.eyJpc3MiOiJzYWtoLmNvbSIsImlhdCI6MTY3ODc3OTUzMiwiZXhwIjoxNjc4NzgzMTMyLCJqdGkiOiJ2NUF2RVJMYWFsdU5DY1ZkTEZ5aTE5eFl6R20tNVBPckk1STVrX05WZXdzIiwidHlwZSI6Imd1ZXN0In0.M2FJY-Ep6Xc51ngDVEzBohKN2hLyiGeVwf6rNBFGAJYphLcRDgxJ-0ekbpYef_H6',
    # 'if-modified-since': 'Tue, 14 Mar 2023 07:38:57 GMT',
    # 'referer': 'https://domik65.ru/flat/lease/420560?search_query=067f2a5e3d2db317462c58d8b8ba269e',
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
