import numbers
import random

def generate_secure_password(lower, upper, numbers, symbols, length):

    if lower:
        lower = "abcdefghijklmnñopqrstuvwxyz"
    else:
        lower = ""
    
    if upper:
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        upper = ""

    if numbers:
        numbers = "0123456789012345"
    else:
        numbers = ""

    if symbols:
        symbols = "!\"#$%&/()=?¡*¨[]_:"
    else:
        symbols = ""

    string = lower + upper + numbers + symbols

    # Generates password
    password = "".join(random.sample(string, int(length)))
    return password



