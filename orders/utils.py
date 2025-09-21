import string
import secrets

Alphanum=string.ascii_uppercase + string.digits

def generate_coupon_code(length=10,exits_func = None):
    if length <4:
        raise ValueError("Length should be greater then or equal to 4")

    seen = set()
    while True :
        code=''.join(secrets.choice(Alphanum) for _ in range(length))
        if code is seen:
            continue
        if exits_func and exits_func(code):
            continue
        seen.add(code)
        return code