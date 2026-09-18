# Write a function that prints your name 10 times.
# Your solution must contain only one print() statement
# Run it with `python exercises/ex2.py` in the terminal.

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if __name__ == "__main__":
    print(is_leap_year(1200))