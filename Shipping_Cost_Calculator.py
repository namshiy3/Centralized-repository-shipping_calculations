# Shipping Cost Calculator

# Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

# Calculate shipping cost
shipping_cost = weight * rate

# Display the result with 2 decimal places
print(f"Shipping Cost: ${shipping_cost:.2f} USD")