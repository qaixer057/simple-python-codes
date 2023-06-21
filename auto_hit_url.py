from urllib.request import urlopen

for i in range(2500):
    with urlopen("URL") as response:
        body = response.read()
        print(type(body))
