import requests

url = "https://api.hh.ru/vacancies"

params = {
    "text": "Программист",
    "area": 1,  # Код Москвы
    "experience": "between1And3",
    "employment": "full",
    "fields": "id,name,area,salary"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    # Вывод информации о найденных вакансиях
    for vacancy in data["items"]:
        salary = vacancy["salary"]
        # salary_info = ""
        if salary:
            salary_from = salary.get('from')
            salary_currency = salary.get('currency')
            print(f"Salary: {salary_from, salary_currency}, ID: {vacancy['id']}, Name: {vacancy['name']}, Area: {vacancy['area']['name']}")
            # print(salary_info)
        else:
            salafy_info = 'N/A'
            print(f"Salary: {salafy_info}, ID: {vacancy['id']}, Name: {vacancy['name']}, Area: {vacancy['area']['name']}")
else:
    print(f"Ошибка {response.status_code}: {response.text}")

