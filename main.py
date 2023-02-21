from pprint import pprint
from utils import load_questions_from_json, draw_table


qustions = load_questions_from_json()
draw_table(qustions)