from datetime import datetime
import json
from typing import TypeAlias, Callable, Literal

class Greeting:
    def __init__(self, greeting_intro: str) -> None:
        self.greeting_intro = greeting_intro
        
    def greet(self, name: str) -> str:
        return f"{self.greeting_intro}, {name}."
    
    def greet_list(self, names: list[str]) -> list[str]:
        greetings: list[str] = [self.greet(name) for name in names]
        return greetings

   
def main():
    current_time = datetime.now()
    if current_time.hour < 12:
        greeting_intro = "Good Morning"
    elif 12 <= current_time.hour < 18:
        greeting_intro = "Good Afternoon"
    else:
        greeting_intro = "Good Evening"
    name = input('Enter your name: ')
    greeting = Greeting(greeting_intro)
    print(greeting.greet(name))
    print(greeting.greet_list(names=["John", "Oscar", "Jack"]))


if __name__ == "__main__":
    main()






        


