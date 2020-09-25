import re

result =[]
with open('./level3.file', "r") as f:
    for line in f:
        data = re.findall('[a-z]{1}[A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]{1}', line)
        result += data
    for item in result:
        print(item[4:5])


