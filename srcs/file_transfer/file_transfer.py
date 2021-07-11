import requests


def print_out(message: str):
    print(message)


def get_ip():
    response = requests.get('https://httpbin.org/ip')
    return response.json()


if __name__ == "__main__":
    print_out('Hello Python.')
