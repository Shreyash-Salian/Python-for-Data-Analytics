"""
========================================== Section A — Concept Application========================================================
========================================== SCENARIO 1 ============================================================================
SCENARIO
You are building a food delivery app that tracks four values per order: the order total (Rs
499.50), the delivery distance (7.3 km), the payment method ('UPI'), and whether the
restaurant is currently accepting orders (True).

Question: Identify the correct Python data type for each of the four values above. Then explain
why assigning the wrong type — for example, storing Rs 499.50 as an integer — would cause an
incorrect result when applying a 10% discount calculation.

"""

# Assigning values
order_total = 499.50
delivery_distance = 7.3
payment_method = "UPI"
restaurant_accepting_orders = True


# Checking data types
print("Order Total:", type(order_total),"-------------",order_total)
print("Delivery Distance:", type(delivery_distance),"---------------",delivery_distance)
print("Payment Method:", type(payment_method),"-------------------",payment_method)
print("Restaurant Status:", type(restaurant_accepting_orders),"----------------------",restaurant_accepting_orders)

discount = order_total * 10 / 100
print(discount)

final_amount = order_total - discount
print("The payable amount is ",final_amount)


print("Original Amount:", order_total)
print("Discount Amount:", discount)
print("Final Amount:", final_amount)


"""
The correct data types are float for order total and delivery distance, string for payment method, and boolean for restaurant status. Choosing the correct data type is important because storing decimal values as integers removes the decimal portion and can lead to incorrect calculations

"""
