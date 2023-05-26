'''Atspausdinkite tą patį teksta taip:
# 1.
# Event: Workshop & Tutorial proposals due
# Date: November 21, 2019

# 2.
# Event: Notification of acceptance
# Date: December 1, 2019

# ir t.t.'''

import re

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

pattern = re.compile(r'(.*(?=(?:\:))):\s([A-Z]\w+\s\d{1,}\,\s\d{4})', re.M)

result = pattern.findall(text)

for num in range(len(result)):
    print(f'{num + 1}.')
    print(f'Event: {"".join(result[num][0])}')
    print(f'Date: {"".join(result[num][1])}')
# print(type(result))
