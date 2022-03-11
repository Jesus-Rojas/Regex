#!/user/bin/python
import re

pattern = re.compile(r'^([\d]{4,4})\-\d\d\-\d\d,(.+),(.+),(\d+),(\d+),.*$')
f = open('./database/fifa.csv', 'r', encoding="utf8")

for line in f:
    res = re.match(pattern, line)
    if res:
        total = int(res.group(4)) + int(res.group(5))
        if total > 30:
            print(f"Goles: {total}, Año: {res.group(1)}, {res.group(2)} ({res.group(4)}) - ({res.group(5)}) {res.group(3)}")

f.close()