"""Entry point for service."""

from utils import process


def main():
    result = process(50)
    print(f"Project: {result}")


if __name__ == "__main__":
    main()
