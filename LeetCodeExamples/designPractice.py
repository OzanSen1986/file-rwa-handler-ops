from typing import Iterable, Protocol

class Transformer(Protocol):
    def transform(self, my_list: Iterable[str]) -> Iterable[str]:
        ...

class Reverser:
    def transform(self, my_list: Iterable[str]) -> Iterable[str]:
        return [word[::-1] for word in my_list]

class Doubler:
    def transform(self, my_list: Iterable[str]) -> Iterable[str]:
        return [f"{word}{word}" for word in my_list]

class Lengthener:
    def transform(self, my_list: Iterable[str]) -> Iterable[str]:
        return [f"{word}:{len(word)}" for word in my_list]


def do_something(transformer: Transformer, my_list: Iterable[str]):
    new_words = transformer.transform(my_list)
    print(new_words)


def main() -> None:
    words = ("code", "python", "ai", "refactor", "bug")
    transformer = Lengthener()
    do_something(transformer, words)

if __name__ == "__main__":
    main()