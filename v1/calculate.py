#  Copyright 2023 Macauley Lim xmachd@gmail.com
#  This code is licensed under GNU AFFERO GENERAL PUBLIC LICENSE v3.0.
#  A copy of this license should have been provided with the code download, if not see https://www.gnu.org/licenses/
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
#  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU AGPL v3.0 for more details.

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