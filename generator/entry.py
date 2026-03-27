import random
import calendar
from generator.common import random_string, get_num_and_file_from_args_or_default, save_to_json
from model.entry import Entry


(num_of_entries, file_name) = get_num_and_file_from_args_or_default(num_default=3, file_default="data/entries.json")

testdata = ([Entry(firstname=random_string("fn", 30),
                   middlename=random_string("mn", 30),
                   lastname=random_string("ln", 30),
                   nickname=random_string("nn", 30),
                   title=random_string("ti", 30),
                   company=random_string("co", 30),
                   address=random_string("nn", 30, use_newline=True),
                   phone_home=random_string("ph", 20),
                   phone_mobile=random_string("pm", 20),
                   phone_work=random_string("pw", 20),
                   email=random_string("e1", 30),
                   email2=random_string("e2", 30),
                   email3=random_string("e3", 30),
                   homepage_url=random_string("ur", 50),
                   birth_day=random.choice([str(x) for x in range(1, 32)] + ["-"]),
                   birth_month=random.choice(list(calendar.month_name)[1:] + ["-"]),
                   birth_year=random_string("", 4),
                   anniversary_day=random.choice([str(x) for x in range(1, 32)] + ["-"]),
                   anniversary_month=random.choice(list(calendar.month_name)[1:] + ["-"]),
                   anniversary_year=random_string("", 4))
             for i in range(num_of_entries)])

save_to_json(testdata, file_name)