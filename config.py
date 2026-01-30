url = "https://api.hh.ru/vacancies"

params1 = {
    "text": "python",
    "area": 1,
    "experience": "between1And3",
    "professional_role": 96,
    "industry": 7,
    "date_from": "2026-01-29",
    "only_with_salary": False,
}

params2 = params1.copy()
params2["experience"] = "noExperience"
