stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}
portfolio = {}
total_investment = 0
print("Welcome to Stock Portfolio Tracker!\n")
print("Available stocks:", ', '.join(stock_prices.keys()))
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock not in stock_prices:
        print("Stock not available. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if stock in portfolio:
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number.")
print("\nYour Portfolio Summary:")
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}")
print(f"\nTotal Investment Value: ${total_investment}")
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == 'yes':
    filename = input("Enter filename (without extension): ")
    with open(f"{filename}.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            value = stock_prices[stock] * qty
            file.write(f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print(f"Portfolio saved to {filename}.txt")
