import string

x = string.digits + string.ascii_letters + string.punctuation

import random

string_code = ''.join([random.choice(x) for i in range(8)])

print(string_code)