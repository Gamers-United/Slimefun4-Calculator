import data, math

data.reinforcedAlloyIngot(16)

print("Raw materials:")
for item in data.cost:
    count = math.ceil(data.cost[item])
    print(f"{item}:{count},",end="")
print("")

print("Level 1 materials:")
for item in data.cost_1:
    count = math.ceil(data.cost_1[item])
    print(f"{item}:{count},",end="")