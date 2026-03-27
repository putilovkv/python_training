from generator.common import random_string, get_num_and_file_from_args_or_default, save_to_json
from model.group import Group


(num_of_groups, file_name) = get_num_and_file_from_args_or_default(num_default=4, file_default="data/groups.json")

testdata = ([Group(name="", header="", footer="")] +
            [
                Group(name=random_string("name", 10),
                      header=random_string("header", 20),
                      footer=random_string("footer", 20))
                for i in range(num_of_groups-1)
            ])

save_to_json(testdata, file_name)