departments = [
    {
        "title": "HR department",
        "employers": [
            {"first_name": "Daniel", "last_name": "Berger", "position": "Junior HR", "salary_rub": 50000},
            {"first_name": "Michelle", "last_name": "Frey", "position": "Middle HR", "salary_rub": 75000},
            {"first_name": "Kevin", "last_name": "Jimenez", "position": "Middle HR", "salary_rub": 70000},
            {"first_name": "Nicole", "last_name": "Riley", "position": "HRD", "salary_rub": 120000},
        ]
    },
    {
        "title": "IT department",
        "employers": [
            {"first_name": "Christina", "last_name": "Walker", "position": "Python dev", "salary_rub": 80000},
            {"first_name": "Michelle", "last_name": "Gilbert", "position": "JS dev", "salary_rub": 85000},
            {"first_name": "Caitlin", "last_name": "Bradley", "position": "Teamlead", "salary_rub": 950000},
            {"first_name": "Brian", "last_name": "Hartman", "position": "CTO", "salary_rub": 130000},
        ]
    },
]

taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]



#вывести названия всех отделов
print(*(department["title"] for department in departments), sep = "\n")

#вывести имена всех работников компании
employers = [[f"{employer['first_name']} {employer['last_name']}" for employer in department['employers']] for department in departments]
for department_members in employers:
  print(*(department_members), sep = "\n")
  
  
#Вывести имена всех сотрудников компании с указанием отдела, в котором они работают
employers = [[f"{employer['first_name']} {employer['last_name']}works in {department['title']}" for employer in department['employers']] for department in departments]
for department_members in employers:
  print(*(department_members), sep = "\n")
  
#Вывести имена всех сотрудников компании, которые получают больше 100к.
employers = [[f"{employer['first_name']} {employer['last_name']}" for employer in department['employers'] if employer['salary_rub'] > 100000] for department in departments]
for department_members in employers:
  print(*(department_members), sep = "\n")
  
#Вывести позиции, на которых люди получают меньше 80к (можно с повторениями).
employers_less_80 = [[employer['position'] for employer in department['employers'] if employer['salary_rub'] < 80000] for department in departments]
for department_members in employers_less_80:
  print(*(department_members), sep = "\n")
  
#Посчитать, сколько денег в месяц уходит на каждый отдел – и вывести вместе с названием отдела
print(*(f"{department['title']}: {sum(employer['salary_rub'] for employer in department['employers'])}" for department in departments), sep = "\n")

#Вывести названия отделов с указанием минимальной зарплаты в нём
salaries_in_departments = {department['title'] : [employer['salary_rub'] for employer in department['employers']] for department in departments}
print(*(f"Минимальная зарплата в {key}: {min(value)}" for key, value in salaries_in_departments.items()), sep = "\n")

#Вывести названия отделов с указанием минимальной, средней и максимальной зарплаты в нём.
print(*(f"Минимальная зарплата в {key}: {min(value)}\nСредняя зарплата в {key}: {sum(value)/len(value)}\nМаксимальная зарплата в {key}: {max(value)}" for key, value in salaries_in_departments.items()), sep = "\n")

#Вывести среднюю зарплату по всей компании.
print(f"Средняя зарплата по всей компании: {sum(sum(value) for value in salaries_in_departments.values())/sum(len(value) for value in salaries_in_departments.values())}")


#Вывести названия должностей, которые получают больше 90к без повторений
employers_more_90 = []
for department in departments:
  for employer in department['employers']:
    if employer['salary_rub'] > 90000:
      employers_more_90.append(employer['position'])
print(*set(employers_more_90), sep = "\n")


#Посчитать среднюю зарплату по каждому отделу среди девушек (их зовут Мишель, Николь, Кристина и Кейтлин)
for department in departments:
  department_women_salaries = []
  for employer in department['employers']:
    if employer['first_name'] in ["Michelle","Nicole", "Christina", "Caitlin"]:
      department_women_salaries.append(employer['salary_rub'])
  print(f"Средняя зарплата среди женщин в отделе {department['title']}: {sum(department_women_salaries)/len(department_women_salaries)}")


#Вывести без повторений имена людей, чьи фамилии заканчиваются на гласную букву.
names_list = []
for department in departments:
  for employer in department['employers']:
    print(employer['last_name'][-1] )
    if employer['last_name'][-1] in "euioay":
      names_list.append(employer['first_name'])
print(*set(names_list), sep = "\n")


#список отделов с суммарным количеством налогов
taxes = [
    {"department": None, "name": "vat", "value_percents": 13},
    {"department": "IT Department", "name": "hiring", "value_percents": 6},
    {"department": "BizDev Department", "name": "sales", "value_percents": 20},
]

taxes_in_departments = {}
taxed_salaries = {}
for department in departments:
  department_name = department['title'].lower()
  taxes_percentage = 0
  for taxes_of_department in taxes:
    if taxes_of_department['department'] == None or taxes_of_department['department'].lower() == department_name:
      taxes_percentage += taxes_of_department['value_percents']
  taxes_in_departments[department_name] = taxes_percentage
  taxes_summ = 0
  for employer in department['employers']:
    taxes_summ += (employer['salary_rub'] * taxes_percentage)/100
  taxed_salaries[department["title"]] = taxes_summ
print(*(f"Сумма налогов, уплачиваемая {key}: {value}" for key, value in taxed_salaries.items()), sep = "\n")

#Вывести список всех сотредников с указанием зарплаты "на руки" и зарплаты с учётом налогов.
for department in departments:
  for employer in department['employers']:
    print(f"Зарплата {employer['first_name']} {employer['last_name']} составляет {employer['salary_rub']}; с учетом налогов: { employer['salary_rub'] - (employer['salary_rub'] * taxes_in_departments[department['title'].lower()])/ 100}")


#Вывести список отделов, отсортированный по месячной налоговой нагрузки.
print(*sorted(taxed_salaries, key=taxed_salaries.get), sep = "\n")

#Вывести всех сотрудников, за которых компания платит больше 100к налогов в год.
for department in departments:
  for employer in department['employers']:
    monthly_taxes = employer['salary_rub'] * taxes_in_departments[department['title'].lower()]/ 100
    if monthly_taxes * 12 > 100000:
      print(f"{employer['first_name']} {employer['last_name']}")
      

#Вывести имя и фамилию сотрудника, за которого компания платит меньше всего налогов
employers_taxes = {}
for department in departments:
  for employer in department['employers']:
    monthly_taxes = employer['salary_rub'] * taxes_in_departments[department['title'].lower()]/ 100
    employers_taxes[f'{employer["first_name"]} {employer["last_name"]}'] = monthly_taxes
print(f"Сотрудник, за которого платят меньше всего налогов: {min(employers_taxes, key = employers_taxes.get)}")