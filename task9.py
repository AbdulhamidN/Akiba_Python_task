exchange_rate = 150

usd_amount = float(input("Enter USD amount: "))

etb_amount = usd_amount * exchange_rate

print("==============================")
print("      CURRENCY EXCHANGE")
print("==============================")
print()
print("USD Amount:", usd_amount)
print()
print("Exchange Rate: 1 USD =", exchange_rate, "ETB")
print()
print("ETB Amount:", etb_amount, "ETB")
print("==============================")