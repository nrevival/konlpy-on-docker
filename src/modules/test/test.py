def get_greeting() -> str:
    return 'Hello [name]'

def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)