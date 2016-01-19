
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

pfs_group2 = cisco_cfg.find_objects(r"set pfs group2")

for line in pfs_group2:
    print "%s are using PFS group2" % line.parent.text 

