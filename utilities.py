import string
import random


def generate_short_url():
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choices(letters, k=6))
