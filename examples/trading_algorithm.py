# Homework

opening_price = 20
percent = 0.20
fund_amount = 10000
high_price = low_price = starting_price

Buy:
If the current_price increase by the percentage, then buy the stock
using the provide funds amount.
if current_price = 24
number_to_buy = fund_amount/current_price [24 buy-in price]
high_price = low_price = 24


Sell:
If the current_price is less than or equal to (1 - percent) = 0.80 of the buy-in or the 
highest price since buying in, then sell all shares.
high_price = low_price = current_price


high_price = 26

current_price = 19

low_price = 19 --> 24



price_list = [ 20, 21, 23, 35, 19, 24, 27, 28 ]

20 
21 wait
23 wait
35 BUY -> H 35 /L 35
19 SELL -> H 19/ L 19
24 BUY -> H 24/ L 24
27 WAIT -> H 27 / L 24
28 WAIT -> H 28 / L 24 
