# Кабинеты

Информация о кабинетах клиники

## Cписок всех кабинетов

**URL** : `/api/cabinet/`

**Method** : `GET`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
[
    {
        "number": 1,
        "owner": "Змиевский Данил Александрович",
        "phone": "+79218765432"
    }
]
```
## Добавить новый кабинет

**URL** : `/api/cabinet/create`

**Method** : `POST`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": 2,
    "owner": "Третьяков Александр Валерьевич",
    "phone": "+79214535677"
}
```
## Просмотр, изменение и удаление кабинета

**URL** : `api/cabinet/<int:pk>/`

**Method** : `GET`, `PUT`, `DELETE`

**Data constraints** : `{}`

**Code** : `200 OK`

**Content** : `{[]}`

```json
{
    "number": 2,
    "owner": "Третьяков Александр Валерьевич",
    "phone": "+79117635567"
}
```