def calbuildingcost(length,width,height,cement_cost,brick_cost):
    volume = length * width * height
    cementTotalcost = cement_cost * volume
    brickTotalcost = brick_cost * volume
    TotalCost = cementTotalcost + brickTotalcost
    return TotalCost
cement_cost_per_bag = 30
brick_cost_per_brick = 10
building_length = 300
building_width = 200
building_height = 50
totalbuildingcost = calbuildingcost(building_length,
                                    building_width,
                                    building_height,
                                    cement_cost_per_bag,
                                    brick_cost_per_brick)
print(f"Total Building Cost:{totalbuildingcost:.2f} units of currency") 