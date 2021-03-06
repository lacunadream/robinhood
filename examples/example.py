from Robinhood import robinhood

with open('auth.txt', 'r') as f:
    username = f.readline()
    password = f.readline()

# Create a robinhood object
r = Robinhood(username, password)

## Get stock price quote
price = r.quote_price("RJET")
print price

## Get full instrument quote object
# q = r.get_quote("RJET")

## Place market order of RJET at best market price
#order_ID = r.place_buy_order("RJET", 3)
#print order_ID

## Place limit order for one share of RJET at $6.24 / share
#order_ID = r.place_buy_order("RJET", 1, "limit", 6.24)
#print order_ID

## Get order details
#print r.order_details(order_ID)

## Cancel an order
#r.cancel_order(order_ID)

## List orders
#orders = r.list_orders()

## Print your current address
#print "Your address is: " + r.address + ", " + r.city + ", " + r.state_residence + " " + r.zipcode

#print r.list_order_details()