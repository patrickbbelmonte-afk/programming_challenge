odd_count = 0

for count in range(10):
    user_number = int(input(f"Enter number {count + 1}: "))
    if user_number % 2 != 0:
        odd_count += 1

print("Number of odd numbers:", odd_count)