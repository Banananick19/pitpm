# ОТЧЕТ USERS API 

* Добавление пользователя

POST http://127.0.0.1:3005/users

body (JSON)

{
    "id": "7d818b16-001c-4c49-87f9-850d55511589",
    "email": "123",
    "password": "12512351",
    "name": "123412",
    "additional_info": "12312",
    "phone": "123412"
}

Приниманиемая информация: OK, статус 200

![img.png](examples/img.png)

* Получение пользователя

GET http://127.0.0.1:3005/users?id=7d818b16-001c-4c49-87f9-850d55511589

Приниманиемая информация: {"id": "7d818b16-001c-4c49-87f9-850d55511589", "email": "123", "password": "12512351", "name": "123412",
"additional_info": "12312", "phone": "123412"}, статус 200

![img_1.png](examples/img_1.png)

* Обновление пользователя

PUT http://127.0.0.1:3005/users/<string:id>

body (JSON)

{
    "email": "1231231321",
    "password": "12512351",
    "name": "123412",
    "additional_info": "12312",
    "phone": "123412"
}
Приниманиемая информация: OK, статус 200

![img_2.png](examples/img_2.png)

* Удаление пользователя

DELETE http://127.0.0.1:3005/users/<string:id>

Приниманиемая информация: OK, статус 200

![img_3.png](examples/img_3.png)


# ОТЧЕТ MUSIC API 

* Добавление музыки

POST http://127.0.0.1:3005/music/<string:id>

form-data
name: file, type: file

Приниманиемая информация: OK, статус 200

![img_4.png](examples/img_4.png)

* Получение музыки

GET http://127.0.0.1:3005/music?id=7d818b16-001c-4c49-87f9-850d55511589

Приниманиемая информация: file, статус 200

![img_7.png](examples/img_7.png)

* Обновление музыки

PUT http://127.0.0.1:3005/music/<string:id>

form-data
name: file, type: file



Приниманиемая информация: OK, статус 200

![img_8.png](examples/img_8.png)

* Удаление музыки

DELETE http://127.0.0.1:3005/music/<string:id>

Приниманиемая информация: OK, статус 200

![img_9.png](examples/img_9.png)
