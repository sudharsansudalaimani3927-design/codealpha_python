stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MICR": 345 
}

stock_name = input("Enter stock name: ").upper()
quantity = int(input("Enter quantity: "))

if stock_name in stocks:
    total_investment = stocks[stock_name] * quantity

    print("Total Investment Value:", total_investment)

    with open("investment.txt", "a") as file:
        file.write(f"Total Investment Value for {stock_name}: {total_investment} \n")

    print("Result saved to investment.txt")

else:
    print("Stock not found!")