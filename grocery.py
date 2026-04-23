T = int(input()) # MOM, WHY DID YOU LET KAREN GET TIKTOK!?
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
        K = int(shop[shop.index(" ") + 1:])
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
            for k in range(len(shopping_list)):
                for m in range(len(inventory)):
                    if inventory[m]["item"] == shopping_list[k]:
                        wanted_items += 1
            print(wanted_items)