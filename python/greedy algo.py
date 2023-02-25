def change(amount):
    coins = [20,10,5,2,1] 
    num_coins = 0
    coin_breakdown = {}  #การเข้า่ถุงdict coin
    for coin in coins:
        coin_breakdown[coin] = 0
        while amount >= coin:
           coin_breakdown[coin] += 1
           amount -= coin
    return coin_breakdown
amount = int(input("Enter amount: "))
coin_of_amount = change(amount)
for i in coin_of_amount:
    if (coin_of_amount[i]):
        print(f"{i}: {coin_of_amount[i]}")