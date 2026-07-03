numbers = [4, 8, 15, 1, 42]

for num in numbers:
    if num < 10:
        numbers.remove(
            num
        )  # modified as its being iterated so its not going to behave as expected

print(f"Filtered numbers: {numbers}")
