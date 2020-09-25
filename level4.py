import requests

value = "12345"
while(1):
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    res = requests.get(url+value)
    text = res.text
    if text == "Yes. Divide by two and keep going.":
        value = str(int(value) / 2)
    else:
        next_value = text.split('nothing is')
        print(next_value[1].strip())
        value = next_value[1].strip()
    