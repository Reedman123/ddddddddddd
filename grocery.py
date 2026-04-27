T = int(input())
best_stores = []
for i in range(T):
    items = input()
    shopping_list = items.split(" ")
    print(shopping_list)
    M = int(input())
    inventory = []
    shops = []
    for j in range(M):
        shop = input()
        name = shop.split(" ")[0]
        K = int(shop.split(" ")[1])
        if K >= 1 and K <= 50:
            wanted_items = 0
            for k in range(K):
                item = input()
                product = item.split(" ")[0]
                price = item.split(" ")[1]
                if "e" in price:
                    base = float(price.split("e")[0])
                    multiplier = float(10 ** float(price.split("+")[1]))
                    price = base * multiplier
                else:
                    price = float(price)
                inventory.append({"item": product, "price": price})
            wanted_items = 0
            for k in range(len(shopping_list)):
                for m in range(len(inventory)):
                    if inventory[m]["item"] == shopping_list[k]:
                        wanted_items += 1
            shops.append({"wanted_items": wanted_items, "inventory": inventory, "name": name})
            print(str(shops[len(shops)-1]["wanted_items"]))
    best_shop = 0
    contenders = []
    for j in range(len(shops)):
        if shops[j]["wanted_items"] > shops[best_shop]["wanted_items"]:
            best_shop = j
        elif shops[j]["wanted_items"] == shops[best_shop]["wanted_items"]:
            contenders.append({"id": j, "better_prices": 0})
    if len(contenders) > 0:
        for i in range(len(shopping_list)):
            best_priceholder = -1
            best_price = -1
            for j in range(len(contenders)):
                inventory = shops[contenders[j]["id"]]["inventory"]
                item_index = -1
                for k in range(len(inventory)):
                    if inventory[k]["item"] == shopping_list[i]:
                        item_index = k
                if item_index >= 0:
                    if best_priceholder < 0:
                        best_priceholder = j
                        best_price = inventory[item_index]["price"]
                    else:
                        if inventory[item_index]["price"] < best_price:
                            best_priceholder = j
                            best_price = inventory[item_index]["price"]
            contenders[best_priceholder]["better_prices"] += 1
        best_shop = 0
        for j in range(len(contenders)):
            if contenders[j]["better_prices"] > contenders[best_shop]["better_prices"]:
                best_shop = contenders[j]["id"]
    best_stores.append(shops[best_shop]["name"])
for i in range(len(best_stores)):
    print(best_stores[i] + "'s prices are top G!!!")