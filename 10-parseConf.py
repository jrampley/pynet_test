
import re
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco.txt")

not_aes = cisco_cfg.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"AES")

for line in not_aes:
    for child in line.children:
        if 'transform' in child.text:
            m = re.search(r"set transform-set (.*)$", child.text)        
            encryption = m.group(1)
    print "  %s >>> %s" % (line.text, encryption)
