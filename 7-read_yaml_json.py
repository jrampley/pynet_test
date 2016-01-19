
import yaml
import json
from pprint import pprint as pp

with open("some_file.yml") as f:
    new_list = yaml.load(f)

print yaml.dump(new_list, default_flow_style=False)

with open("some_file.json") as f:
    new_json_list = json.load(f)

pp (new_json_list)
