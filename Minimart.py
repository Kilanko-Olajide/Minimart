items_and_price = {"banana": 300,
                   "cherry": 50, 
                   "mango" : 100, 
                   "pineapple" : 700, 
                   "apple" : 300, 
                   "orange" : 100}

cart = []
total = 0
print("--------MENU--------")
for keys, values in items_and_price.items():
    print(f"{keys:10} : {values}")


while True:
    fruit_to_buy = input("What fruit do you want to buy: ")
    if items_and_price.get(fruit_to_buy) is not None:
        cart.append(fruit_to_buy)
    elif fruit_to_buy.lower() == "q":
        break

for items in cart:
    total += items_and_price.get(items)
    print(items, end=" ")

print(f"Your total is {total} naira.")

