import random
import string

def generate_random_email(domain="yandex.ru"):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{random_string}@{domain}"