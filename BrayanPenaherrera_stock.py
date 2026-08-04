# BrayanPenaherrera_stock.py
# Name: Brayan Penaherrera
# Date: 03/19/2026
# Program: stock.py
# Description: This is a program that calculates the profit or loss from buying and sellin stock,
# including commissions paid during purchase and sale.

# ===============
# CONSTANTS
# ===============
COMMISSION_RATE = 0.0325

# ===============
# INPUT
# ===============
shares_purchased = int(input("Please enter the number of shares purchased: "))
purchase_price = float(input("Please enter the price paid per share: "))

shares_sold = int(input("Please enter the number of shares sold: "))
selling_price = float(input("Please enter the selling price per share: "))

# ===============
# PROCESSING
# ===============
amount_paid = shares_purchased * purchase_price
commission_purchased = amount_paid * COMMISSION_RATE

amount_sold = shares_sold * selling_price
commission_sale = amount_sold * COMMISSION_RATE

profit = amount_sold - commission_sale - amount_paid - commission_purchased

# ===============
# OUTPUT
# ===============
print("\nAmount paid for the stock: $" + format(amount_paid, ".2f"))
print("Commission paid on the purchase: $" +
      format(commission_purchased, ".2f"))

print("\nAmount the stock sold for: $" + format(amount_sold, ".2f"))
print("commission paid on the sale: $" + format(commission_sale, ".2f"))

print("\nProfit (or loss if negative): $" + format(profit, ".2f"))
