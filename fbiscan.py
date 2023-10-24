import sys
import re
with open("namefile FBI.mhtml", "r") as f:
    for line in f:
        if re.search(sys.argv[1], line):
            print(line)

print("end")