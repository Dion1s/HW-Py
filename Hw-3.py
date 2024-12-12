from typing import Generator, List

def odd_numbers_in_range(start: int, end: int) -> Generator[int, None, None]:
    for number in range(start, end):
        if number % 2 != 0:
            yield number

def values_outside_range(lst: List[int], start: int, end: int) -> Generator[int, None, None]:
    for number in lst:
        if number < start or number >= end:
            yield number

if __name__ == "__main__":
    # Task 1
    print("Непарні числа у діапазоні 1-10:")
    for odd in odd_numbers_in_range(1, 10):
        print(odd, end=" ")

    print("\n\nЧисла, що не належать діапазону 5-15 у списку [1, 3, 5, 10, 20, 25]:")
    # Task 2
    for value in values_outside_range([1, 3, 5, 10, 20, 25], 5, 15):
        print(value, end=" ")