
import yaml
import json

my_list = range(8)
my_list.append({})
my_list[-1]['chasis_config1'] = {}
my_list[-1]['models'] = ['9006', '9010']
my_list[-1]['processor'] = 'A9K-RSP-4G'
my_list[-1]['software'] = '4.2.3'
my_list[-1]['trident'] = ['A9K-4T-L', 'A9K-8T-L', 'A9K-8T-B', '9K-40GE-L', 'A9K-2T20GE-L', 'A9K-16T/8-B']
my_list.append({})
my_list[-1]['chasis_config2'] = {}
my_list[-1]['models'] = ['9006', '9010']
my_list[-1]['processor'] = 'A9K-RSP-4G'
my_list[-1]['software'] = '5.1.3'
my_list[-1]['trident'] = ['A9K-4T-L', 'A9K-8T-L', 'A9K-8T-B', '9K-40GE-L', 'A9K-2T20GE-L', 'A9K-16T/8-B']



print yaml.dump(my_list, default_flow_style=False)

with open("some_file.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open("some_file.json", "w") as f:
    json.dump(my_list, f)
