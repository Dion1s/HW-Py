# #Task 1-2
# fruits: tuple = ("banana", "apple", "bananamango", "mango", "strawberry-banana", "apple", "apple-orange")

# print("Enter part of the fruit name: ")
# fruit_part: str = input().lower()

# count: int = 0
# print("Matching fruits:", end=" ")
# for fruit in fruits:
#     if fruit_part in fruit.lower():
#         print(fruit, end=" ")
#         count += 1

# print(f"\nTotal partial matches: {count}")

# #Task 3
# manufacturers: tuple = ("Toyota", "Ford", "Tesla", "Toyota", "BMW", "Ford")

# print("Enter the name of the manufacturer to replace: ")
# target: str = input()

# print("Enter the replacement word: ")
# replacement: str = input()

# updated_manufacturers: tuple = tuple(
#     replacement if manufacturer == target else manufacturer
#     for manufacturer in manufacturers
# )

# print("Updated manufacturers tuple:", updated_manufacturers)

#Task 4
from typing import Tuple, Dict

def count_digits_statistics(numbers: Tuple[int, ...]) -> Dict[int, int]:
    digit_count: Dict[int, int] = {}
    
    for number in numbers:
        digits: int = len(str(abs(number)))  
        digit_count[digits] = digit_count.get(digits, 0) + 1
    
    return digit_count

numbers: Tuple[int, ...] = (1, 12, 123, 4, 56, 789, 101, 99)
statistics: Dict[int, int] = count_digits_statistics(numbers)

for digit, count in sorted(statistics.items()):
    print(f"{digit} цифра — {count} елементів")

#Task 5
from typing import Callable, Any

def correct_negative_numbers(func: Callable) -> Callable:
    def wrapper(*args: Any, **kwargs: Any) -> Any:

        corrected_args = tuple(arg if not isinstance(arg, (int, float)) or arg >= 0 else 1 for arg in args)
        

        corrected_kwargs = {
            key: value if not isinstance(value, (int, float)) or value >= 0 else 1
            for key, value in kwargs.items()
        }
        
        return func(*corrected_args, **corrected_kwargs)
    
    return wrapper

@correct_negative_numbers
def func(*args: Any, **kwargs: Any) -> None:
    print("Позиційні аргументи:", args)
    print("Іменовані аргументи:", kwargs)

func(10, -3, "red", -1, 200, color="blue", size=-5, price=-100)

