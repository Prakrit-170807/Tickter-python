#enter prices of one pack of each chocolate
DairyMilkPrice = 20
KitKatPrice = 25
EclairPrice = 2
#ask user how many of each chocolate they bought
DairyMilk = int(input('How many Dairy Milks?'))
KitKat = int(input('How many KitKats?'))
Eclair = int(input('How many Eclairs?'))
#calculate total cost for each chocolate as No.of chocolates x price of chocolate
DairyMilkCost = DairyMilkPrice * DairyMilk
KitKatCost = KitKatPrice * KitKat
EclairCost = EclairPrice * Eclair
#add the cost for each chocolate to get total cost
TotalCost = DairyMilkCost + KitKatCost + EclairCost
#print total cost
print("You pay:",TotalCost)
