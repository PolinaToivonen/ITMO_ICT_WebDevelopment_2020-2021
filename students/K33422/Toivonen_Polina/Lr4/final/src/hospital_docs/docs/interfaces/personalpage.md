# Личный кабинет

В верхней части страницы расположено меню, в котором авторизованный 
пользователь может: 
<li>Вернуться на главную (но зачем ему это?)</li>
<li>Зайти в личный кабинет (встречает пользователя по умолчанию)</li> 
<li>Посмотреть список зарегистрированных пациентов</li>
<li>Посмотреть список кабинетов</li>
<li>Посмотреть список предоставляемых услуг</li>
<li>Посмотреть базу данных с диагнозами</li>
<li>Выйти их аккаунта</li>

## Персональные данные

В этом разделе находится карточка, в которой выведена вся информация о пользовалеле, доступная при регистрации.
Под карточкой с информацией находятся 2 кнопки:
<li><b>Изменить (данные)</b> - позволяющая редактировать информацию профиля</li>
<li><b>Удалить</b> - позволяющая удалить профиль (для подтверждения удаления необходимо ввести пароль)</li> 

URL : `/personalpage`

Methods : `GET`, `PATCH`, `DELETE`

Success Responses Code : `200 OK`