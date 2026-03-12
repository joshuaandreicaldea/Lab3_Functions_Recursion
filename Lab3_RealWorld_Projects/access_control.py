# access_control.py

def monitor(func):
    def wrapper(*args, **kwargs):
        print("Authorization Started")
        result = func(*args, **kwargs)
        print("Authorization Completed")
        return result
    return wrapper


def compute_access_level(control_num, favorite_artist):
    return control_num * 3 + len(favorite_artist)


@monitor
def validate_access(access_level, control_num):
    threshold = control_num * 5

    if access_level >= threshold:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"