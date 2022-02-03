
#Задание №1
1) Выведите в результате запроса имя, должность и зарплату работника с должностью
директор
>SELECT staff.user_name, bussines.position_name, bussines.salary 
> 
>FROM bussines JOIN staff 
> 
>ON bussines.position_id = staff.position_id WHERE bussines.position_name='Директор';
> >| 1 | Владимир | Директор | 3000 |


2) Посчитайте сумму зарплат всех инженеров

>SELECT SUM(bussines.salary) 
> 
>FROM bussines JOIN staff 
> 
>ON bussines.position_id = staff.position_id WHERE bussines.position_name='Инженер';
> > | 1 | 3000 |
  
3) Посчитайте среднюю зарплату работников с именем на букву “А”
>
>SELECT AVG(bussines.salary)
> 
>FROM bussines JOIN staff
> 
>ON bussines.position_id = staff.position_id WHERE staff.user_name LIKE 'А%';
> > | 1 | 1166.6666666666666667 | 
> 
 
#Задание №2
1) Выполните скрипт start.sh
> home/user/scripts/start.sh
2) Выведите в терминал информацию о пользователе u1 из файла логов user.logs
> cat home/user/logs/user.logs | grep u1 
3) Найдите id процесса u_proc и убейте его
> >pgrep u_proc
> 
>  35567
> 
> >kill SIGKILL 35567
> 
> or
> 
> >kill -9 35567
 
#Задание №3

>workers = ["Андрей", "Николай"]
>
>workers.append("Анатолий")
>
>workers.append("Олег")
>
>for worker in workers:
>
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f"У нас работает {worker}")
>

 
#Задание №4

>Решение находится в файле "news_parser.py".

 
#Задание №5

1)
> Успешно выполнился перый запрос, т.к. имеет статус-код 200.
2)
> Во втором запросе возникла 500я ошибка - ошибка на стороне сервера при обработке запроса.
>
> При третьем запросе возникла ошибка 404, говорящяя о неправильно составленом запросе.

#Задание №6

>Добрый день. Информация о возникшей проблемме передана разработчикам, 
> и в скором времени будет решена. 
> В качестве временного решения предлогаю включить режим планирования:
> > Настройки => режим планирования &#9745;  

 
#Задание №7

>
>On November 23, on Monday, at 9:00 an accident occurred on the server
> "serv1" (Server is not available).
> We ask you to involve the developer on duty to solve the problem.

 
