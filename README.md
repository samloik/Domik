
 Функция получения номеров по идентификатору контакта через api сайта https://domik65.ru/

 Важно!!!

 Необходимо указывать точные (указанные на сайте) номера контактов, иначе сервер распознает
 неверные запросы и блокирует авторизацию по IP адресу на некоторое время (около часа).


    git clone https://github.com/samloik/Domik.git
    cd Domik

    pip install -r requirements.txt


 Пример использования:



    from domik import get_phone_number
    
    print(get_phone_number('709088'))



 