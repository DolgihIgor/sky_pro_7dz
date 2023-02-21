import json


def load_questions_from_json():
    """ Считывает данные из файла .json"""
    file = open("data.json", "r", encoding="utf-8")
    data = json.load(file)
    file.close()
    return data


def draw_table(questions):
    """ Рисует таблицу по данным файла json"""
    for category_name, category_questions in questions.items():
        print(category_name.ljust(17), end="")
        for price, question_data in category_questions.items():
            asked = question_data["asked"]
            if not asked:
                print(str(price).ljust(5), end=" ")
            else:
                print("   ".ljust(5), end=" ")
        print()
