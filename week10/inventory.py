# Reflection:
# 1. The most surprising thing about Python lists is how flexible and dynamic they are—unlike fixed-size arrays in other programming languages, Python lists can easily grow or shrink, hold mixed data types, and come packed with built-in methods like .append(), .remove(), and .sort() right out of the box.
# 2. In a past retail inventory tracking project, doing manual updates and calculations in Excel for hundreds of stock items was tedious and prone to human error. Using a Python list and accumulator loops would have automated the calculations and filtering instantly, saving hours of repetitive sorting and calculation.

# EXERCISE 1 · Beginner: Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("-" * 40)

# EXERCISE 2 · Beginner: Index practice

print(inventory[0])
print(inventory[-1])
middle_index = len(inventory) // 2
print(inventory[middle_index])

print("-" * 40)

# EXERCISE 3 · Beginner: Slicing

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

print("-" * 40)

# EXERCISE 4 · Intermediate: Modify

inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("-" * 40)

# EXERCISE 5 · Intermediate: Tuple comparison

coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError:
    print("TypeError caught: Tuples are immutable, which is useful for coordinates because it ensures fixed data like geographic locations cannot be accidentally modified during program execution.")
print(coords)

print("-" * 40)

# EXERCISE 6 · Intermediate: Average of a list of sales

sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_sale = max(sales)
worst_sale = min(sales)

print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_sale} | Worst: {worst_sale}")

print("-" * 40)

# EXERCISE 7 · Intermediate: Accumulator pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for p in prices:
    discounted.append(round(p * 0.9, 2))

print("Original prices:", prices)
print("Discounted prices:", discounted)

print("-" * 40)

# EXERCISE 8 · Advanced: Filter above threshold

sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales_data:
    if s > 300:
        high_sales.append(s)

high_count = len(high_sales)
high_avg = sum(high_sales) / high_count

print(f"{high_sales} | Count: {high_count} | Avg: ~{round(high_avg, 2)}")