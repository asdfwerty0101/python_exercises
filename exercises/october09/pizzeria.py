from pstats import add_func_stats

item1_name  = "Маргарита"
item1_price = 2200
item1_qty   = 2
item1_sum = item1_price * item1_qty
print(f"Item [{item1_name}] amount is {item1_sum}")

item2_name  = "Пепперони"
item2_price = 2700
item2_qty   = 1
item2_sum = item2_price * item2_qty
print(f"Item [{item2_name}] amount is {item2_sum}")

item3_name  = "Кола 1л"
item3_price = 700
item3_qty   = 3
item3_sum = item3_price * item3_qty
print(f"Item [{item3_name}] amount is {item3_sum}")

item4_name  = "Чизкейк"
item4_price = 1500
item4_qty   = 2
item4_sum = item4_price * item4_qty
print(f"Item [{item4_name}] amount is {item4_sum}")

total_items_sum = item1_sum + item2_sum + item3_sum + item4_sum
print(f"total amount of all items is {total_items_sum}")

delivery         = True
delivery_price   = 800
discount_percent = 10

discount_sum = total_items_sum // 100 * discount_percent
print(f"amount of discount 10% is {discount_sum}")

total_items_sum_with_discount = total_items_sum - discount_sum
print(f"total items sum with 10% discount is {total_items_sum_with_discount}")

if delivery == True:
    total_items_sum_with_discount_and_delivery =             total_items_sum_with_discount + delivery_price
else:
    total_items_sum_with_discount_and_delivery = total_items_sum_with_discount

item_avg_price = total_items_sum // 4
print(f"Average price of the item in the order is {item_avg_price}")





