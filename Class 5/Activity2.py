buy=int(input("Enter buying price:"))
sell=int(input("Enter selling price:"))
if sell>=buy:
    print("You are in profit",sell-buy)
else:
     print("You are in loss",buy-sell)