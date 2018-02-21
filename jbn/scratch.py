import requests
from os import getcwd


def main():
    r = requests.get("https://chicagohealth.herokuapp.com/api/v1/places")

    with open(getcwd() + "/response.json", 'w') as f:
        f.write(r.text)

if __name__ == '__main__':
    main()
