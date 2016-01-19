
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

crypto_map = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for line in crypto_map:
    print line.text
    for child in line.children:
        print child.text
