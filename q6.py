item_prices = [10.00, 15.00, 20.00] 
item_quantities = [2, 1, 3] 
discount_rate = 10
tax_rate = 5  
total_price = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))
discount_amount = total_price * (discount_rate / 100)
price_after_discount = total_price - discount_amount
tax_amount = price_after_discount * (tax_rate / 100)
final_total_cost = price_after_discount + tax_amount
print(f"Total price before discount: ${total_price:.2f}")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"Price after discount: ${price_after_discount:.2f}")
print(f"Tax amount: ${tax_amount:.2f}")
print(f"Final total cost: ${final_total_cost:.2f}")
