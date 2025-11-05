from datetime import datetime
from collections.abc import Callable, TypeAlias
from functools import partial

GreetingReader: Callable[[], str]
GreetingFunction: Callable[[str], str]

def greet(name: str, greeting_reader: GreetingReader) -> str:
    if name == "OZAN":
        return "Hello, OZAN! Welcome back!"
    return f"{greeting_reader()}, {name}"

def greet_list(names: list[str], greeting_fn: GreetingFunction) -> list[str]:
    return [greeting_fn(name) for name in names]

def read_greeting() -> str:
    current_time = datetime.now()
    if current_time.hour < 12:
        return "Good Morning"
    elif 12 <= current_time.hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

def read_name() -> str:
    return input('Enter your name: ')


def main():
    greetFn = partial(greet, greeting_reader=read_greeting)
    print(greetFn(read_name()))
    print(greet_list(["JOHN", "JANE", "WILLIAM"], greetFn))

if __name__ == "__main__":
    main()






        


