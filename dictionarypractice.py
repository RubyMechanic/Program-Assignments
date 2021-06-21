food_prices = {"chicken":1.59, "beef":1.99, "cheese":1.00, "milk":2.50}
NBA_players = {"Lebron James": 23, "Kevin Durant":35, "Stephen Curry":30, "Damian Lillard":0}

def nba_numbers(player, formula):
    number = NBA_players[player]*formula-NBA_players[player]+1
    
    print(player + "'s new jersey number is " + str(number))

nba_numbers("Kevin Durant", 3)
nba_numbers("Lebron James", 2)
chicken_price = food_prices["chicken"]
print(chicken_price)
beef_price = food_prices["beef"]
print(beef_price)
cheese_price = food_prices["cheese"]
print(cheese_price)
milk_price = food_prices["milk"]
print(milk_price)

def total_price(itemone, itemtwo):
    price = food_prices[itemone]+food_prices[itemtwo]
    print("The total price of chicken and cheese is ")
    print(price)
    

def price_difference(oneitem, otheritem):
    price = food_prices[oneitem] - food_prices[otheritem]
    print("the difference between the prices of chicken and cheese is ")
    print(price)

NBA_players["Lebron James"] = 6
lebron_number = NBA_players["Lebron James"]
print(lebron_number)
NBA_players["Lebron James"] -=17
lebron_number = NBA_players["Lebron James"]
print(lebron_number)

shoes = {"Jordan 13":1, "Yeezy": 8, "Foamposite": 10, "AirMax":5, "SB Dunk":20}
def restock(shoe, x):
    shoes[shoe] = shoes[shoe] *x
    print(shoes)

restock("Yeezy", 4)
restock("Jordan 13", 20)
restock("Foamposite", 3)
restock("AirMax", 6)
restock("SB Dunk", 2)
price_difference("chicken", "cheese")
total_price("chicken", "cheese")
def destock(shoe, x):
    if shoes[shoe]>30:
        shoes[shoe] = shoes[shoe]/x
        print(shoes)
    elif shoes[shoe]<= 30:
        shoes[shoe] = shoes[shoe]*x

destock("SB Dunk", 5)
destock("Jordan 13", 4)
