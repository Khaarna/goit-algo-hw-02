from collections import deque


def is_palindrome(s: str) -> bool:
    cleaned = s.replace(" ", "").lower()
    dq = deque(cleaned)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False

    return True


def main():
    test_cases = [
        "racecar",
        "abba",
        "A man a plan a canal Panama",
        "hello",
        "Was it a car or a cat I saw",
        "No lemon no melon",
        "",
        "a",
    ]

    for s in test_cases:
        result = is_palindrome(s)
        print(f"{'Yes' if result else 'No':3} | \"{s}\"")


if __name__ == "__main__":
    main()
