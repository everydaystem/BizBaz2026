scores = [80, 90, 95, 85]
total = 0

for score in scores:
    total += score
    average = total / len(scores)

print(f"Average: {average}")  # unbound average var
