Программа учета регламентных работ и ремонта.

Данная программа предназначена для учета работ проходящих на площадках предприятий. Бригада ремонта и ТО получает задание и работает над его выполнением.

Технологии.
Python 3.9
Представление :
asgiref==3.8.1
Django==5.1.3
sqlparse==0.5.2
tzdata==2024.2

Чтобы проект работал нужно:
Установить Django: pip install django

![2024-12-19_18-51-25](https://github.com/user-attachments/assets/022b7ad7-3653-4ce1-bc98-60495474e5d2)
Импортировать openpyxl и datetime
pip install openpyxl
pip install datetime

Приложение запускается командой: python manage.py runserver


![2024-12-19_18-59-03](https://github.com/user-attachments/assets/5de6a580-8769-43ef-9337-f521dc2d7163)

Структура проекта

нажмите на  http://127.0.0.1:8000/ 
откроется авторизация логин admin пароль 123

![2024-12-20_19-19-53](https://github.com/user-attachments/assets/fb30012d-8239-4bc8-90fa-bb3eeb4ebe69)



откроется приложение
![2024-12-19_19-03-21](https://github.com/user-attachments/assets/ff5982f6-434b-4517-8f36-c34b3721366f)
Первы пункт меню "Сотрудники"
![2024-12-19_19-06-02](https://github.com/user-attachments/assets/9c503b1d-ffa4-4120-a3c0-81aed664fecd)
У списка сотрудников есть кнопка добавить ![2024-12-19_19-08-26](https://github.com/user-attachments/assets/6935b455-113c-43ee-9ba4-b5eb45f75976)
 нажав её вы перехродите в форму добавления
 ![2024-12-19_19-18-36](https://github.com/user-attachments/assets/4615e317-8eb0-4791-8ed0-98764d598bc5)
 при правильнро заполненной форме выйдет сообщение
![2024-12-19_19-23-29](https://github.com/user-attachments/assets/9a28388a-8192-42c9-9b55-bca64f49fcf6)
при нажатии вернуться возщвращаемся к списку
![2024-12-19_19-25-40](https://github.com/user-attachments/assets/b0e1cf87-123a-4639-ba45-f9b20cdc7423)
сотрудника можно отредактировать нажам на ![2024-12-19_19-27-08](https://github.com/user-attachments/assets/23db12b9-c1cf-4506-8f29-ad188ac84d4a)
![2024-12-19_19-40-15](https://github.com/user-attachments/assets/69563a8c-aafe-4a85-81e3-4d905d3e7177)
при изменении нажать "Сохранить"
Выйдя в главное меню нажмите "Площадки" это перечень производственных площадок на которых требуется ремонт.
![2024-12-19_19-49-00](https://github.com/user-attachments/assets/56fa0780-dd2b-4278-9aae-e0269637d65f)
нажав на кнопку ![2024-12-19_19-08-26](https://github.com/user-attachments/assets/644bb6ec-af57-46f8-9871-b56a4be68fce) можно добавить площадку 
![2024-12-19_19-58-42](https://github.com/user-attachments/assets/39ef94d9-fbc3-442c-8cea-c0d395d1e281)
при успешном вводе выйдет сообщение
![image](https://github.com/user-attachments/assets/f98f22b7-4156-41f0-9985-833190667834)
"Вернуться" возвращяемся к списку
![2024-12-19_20-03-03](https://github.com/user-attachments/assets/6f7c36a0-1c15-42ef-ad28-56dc4c5d6902)
В главном меню нажимаем "Участки" и выходим к списку ремонтов и их исполнителей
![2024-12-19_20-07-21](https://github.com/user-attachments/assets/22f4cee0-5740-4da5-9962-dfffa823a2b4)
по кнопке ![2024-12-19_19-08-26](https://github.com/user-attachments/assets/13022891-e3f0-462e-b24a-1c24d5f703a4)
  можно добавить новый ремонт

  ![2024-12-19_20-12-50](https://github.com/user-attachments/assets/7fab3893-2acf-40e5-950a-535f3de8d808)

  при успешном внесении данных выйдет сообщение

  ![2024-12-19_20-14-01](https://github.com/user-attachments/assets/781fbe79-befc-4fc6-85a1-62e2a60830ab)

"Вернуться" возвращяемся к списку ремонтов

![2024-12-19_20-16-42](https://github.com/user-attachments/assets/67e46b15-9d19-467f-8565-cde02745948b)

самый последний ремонт в верхнем списке и у него пока нет исполнителей. С помощью кнопок можно сортировать и накладывать фильтр по дате
кнопкой ![2024-12-19_20-23-16](https://github.com/user-attachments/assets/fec16d25-f606-4580-9c15-2bca6066f408) можно открыть форму и завершить ремонт

![2024-12-19_20-24-42](https://github.com/user-attachments/assets/dedc8264-078b-45a9-b0ea-1143920e8b97)

нужно ввести корректно дату и пароль администратора при правильном завершении выходим в список ремонтов.

![2024-12-19_20-27-54](https://github.com/user-attachments/assets/1b90e4b1-66d3-46b5-8f6f-222dc4925584)

нажав на "Работы" переходим к списку исполнителей и объектов ремонта

![2024-12-19_20-31-41](https://github.com/user-attachments/assets/c749057a-b8c5-49a2-82dd-62cb3d04b1fd)

по кнопке ![2024-12-19_19-08-26](https://github.com/user-attachments/assets/fd33dff6-2baa-4e43-9959-76689a1af281) добавляем работу

![2024-12-19_20-36-43](https://github.com/user-attachments/assets/cd506f09-ade5-4d16-a909-3b05bc3a4503)

из списка открытых ремонтов выбираем ремонт, исполнителя, объект ремонта, назначаем исполнителя руководителем ремонта или ТО
указываем дату окончания начала. При правильном внесении выйдет сообщение

![2024-12-19_20-41-00](https://github.com/user-attachments/assets/ac94aa70-9777-4338-a1c5-315629dfe664)

возвращаемся к списку работ

![2024-12-19_20-43-01](https://github.com/user-attachments/assets/40dcd67f-dbe8-4009-96fd-8217621b276c)

работа добавлена в списке ремонтов появится позиция работ

![2024-12-19_20-47-00](https://github.com/user-attachments/assets/4ab8e98f-fc5d-41ad-8b9c-04a2d5974797)

работа завершается по кнопке ![2024-12-19_20-23-16](https://github.com/user-attachments/assets/f239f5c2-5292-473a-89ad-9cdf904958a7)

при внесении даты, комментария и пароля администратора работа закрывается по кнопке "подтвердить"

![2024-12-19_20-50-15](https://github.com/user-attachments/assets/41c942ad-b769-4756-939d-f364f1d402a3)

переходим в работы и видим, что работа завершена

![2024-12-19_20-53-39](https://github.com/user-attachments/assets/b21217ba-9142-4121-b1b0-1dc061a0e4b0)

по ![2024-12-19_20-54-47](https://github.com/user-attachments/assets/9dc8f26c-c1f7-4d5a-a258-857fc4d84299) можно развернуть комментарий к ремонту

![2024-12-20_19-30-16](https://github.com/user-attachments/assets/7238f789-744d-47f8-9b62-800d8bf7da44)



форму можно фильтровать и сортировать а так же выгрузить в Excel по кнопке если нужно задав интервал 
![2024-12-19_20-58-53](https://github.com/user-attachments/assets/44b15dbf-075b-444b-87e0-612d42b0e52d)

![2024-12-19_21-00-57](https://github.com/user-attachments/assets/37e8d4be-c851-4b8e-94ed-18ae13c71d5f)

Администратор открывает аккаунт супервизора 
Доступ администратора:
логин: admin
пароль: 123

![2024-12-19_21-04-37](https://github.com/user-attachments/assets/42db8a30-125f-4c23-b010-6a15b94df31b)

![2024-12-19_21-31-54](https://github.com/user-attachments/assets/42078244-530f-4a34-a6d8-2974ba597741)

Шаблоны страниц

meunu.html - базовый шаблон
employee.html - список сотрудников
regictration_page.html - регистрация сотрудника
edit_employee.html - редактирование сотрудника
equipment.html - список площадок
registration_equipment.html - регистрация площадки
repair.html - список объектов для ремонта
registration_repair.html - регистрация ремонта
complete_repair.html - завершение ремонта
task.html - список задач ремонта
registration_task.html - назначение исполнителя на площадку ремонта
complect_task.html - завершение задачи исполнителя ремонта


Разработчик Савченков П.В.

