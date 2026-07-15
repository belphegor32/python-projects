import sys

def main():
    say_hello(input("Name: "))


def say_hello(name: str) -> None:
    print(f"Hello {name}")


if __name__ == "__main__":
    main()