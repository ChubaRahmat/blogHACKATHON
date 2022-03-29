import uuid


def get_random_num():
    num = str(uuid.uuid4())[:8].replace('-', '').lower()
    return num