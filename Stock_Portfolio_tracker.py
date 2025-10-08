stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 130
}

print("Available Stocks:", ", ".join(stock_prices.keys()))

portfolio = {}
while True:
    stock = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("❌ Stock not found in list. Try again.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("❌ Please enter a valid number.")

total_value = 0
print("\nYour Portfolio Summary:")
print("-" * 40)
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = qty * price
    total_value += value
    print(f"{stock:<10} Qty: {qty:<5} Price: ${price:<6} Value: ${value:<8}")

print("-" * 40)
print(f"💰 Total Investment Value: ${total_value}")

save = input("\nDo you want to save this portfolio? (y/n): ").lower()
if save == 'y':
    file_type = input("Save as 'txt' or 'csv'?: ").lower()
    if file_type == 'txt':
        with open("portfolio.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("-" * 40 + "\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares @ ${stock_prices[stock]} each\n")
            f.write(f"\nTotal Investment: ${total_value}\n")
        print("✅ Portfolio saved as 'portfolio.txt'")
    elif file_type == 'csv':
        import csv
        with open("portfolio.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], qty * stock_prices[stock]])
            writer.writerow(["Total", "", "", total_value])
        print("✅ Portfolio saved as 'portfolio.csv'")
    else:
        print("❌ Invalid choice. File not saved.")
