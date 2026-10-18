"""
Self-Assessment Answers:
1. In Exercise 5, the first bug spotted was typically a syntax or indentation error identified directly from the traceback. This highlights that reading error tracebacks carefully provides an immediate roadmap to the issue before needing print statements or external help.
2. apply_discount takes a numerical price and a string representing the discount tier ("gold", "silver", "bronze", or any other value) as inputs. It evaluates the tier and returns the discounted price as a float. A colleague could easily use it without reading the internal body because the function name and parameters are descriptive.
3. AI Disclosure: No AI used.
"""

# --- Exercise 1 ---
def calculate_tax(price, rate):
    return price * rate

tax_1 = calculate_tax(100, 0.07)
tax_2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax_1:.2f}")
print(f"Tax on $250 at 8%: ${tax_2:.2f}")


# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

test_price = 200
print(f"gold:   ${apply_discount(test_price, 'gold'):.2f}")
print(f"silver: ${apply_discount(test_price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(test_price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(test_price, 'none'):.2f}")


# --- Exercise 3 ---
base_price = 200
discounted = apply_discount(base_price, "gold")
print(f"After gold discount: ${discounted:.2f}")
final_with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After tax: ${final_with_tax:.2f}")

def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax_amount = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax_amount

print(f"final_price(200, \"gold\", 0.07) = ${final_price(200, 'gold', 0.07):.2f}")


# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---
def calculate_total_sales(sales_list):
    total = 0.0
    for sale in sales_list:
        total += sale
    return total

sample_sales = [50.0, 30.0, 20.0]
print(f"Fixed broken_sales total: ${calculate_total_sales(sample_sales):.2f}")


# --- Exercise 6 ---
x = 100 

def double_it():
    x = 999   
    return x * 2

print(x)           
print(double_it()) 
print(x)           