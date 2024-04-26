cost = {}
cost_1 = {}
cost_2 = {}
cost_3 = {}
cost_4 = {}

def networkCapacitor1(count):
    opticGlass(4.0*count)
    opticCable(4.0*count)
    carbonadoEdgedEnergyCapacitor(count)

def carbonadoEdgedEnergyCapacitor(count):
    carbonado(count*4)
    redstone(count*2)
    redstoneAlloyIngot(count*2)
    largeEnergyCapacitor(count)

def carbonado(count):
    rawCarbonado(count)

def rawCarbonado(count):
    glassPane(count)
    carbonChunk(count)
    syntheticDiamond(count)

def syntheticDiamond(count):
    carbonChunk(count)

def carbonChunk(count):
    flint(count)
    compressedCarbon(count*8)

def largeEnergyCapacitor(count):
    bigEnergyCapacitor(count)
    redstone(count*2)
    redstoneAlloyIngot(count*2)
    reinforcedAlloyIngot(count*4)

def reinforcedAlloyIngot(count):
    damascusSteelIngot(count)
    hardenedMetal(count)
    corinthianBronzeIngot(count)
    solderIngot(count)
    billionIngot(count)
    goldIngot24(count)

def corinthianBronzeIngot(count):
    copperDust(count)
    bronzeIngot(count)
    goldDust(count)
    silverDust(count)

def solderIngot(count):
    leadIngot(count)
    leadDust(count)
    tinDust(count)

def goldIngot24(count):
    goldIngot22(count)
    goldDust(count)

def goldIngot22(count):
    goldIngot20(count)
    goldDust(count)

def goldIngot20(count):
    goldIngot18(count)
    goldDust(count)

def goldIngot18(count):
    goldIngot16(count)
    goldDust(count)

def goldIngot16(count):
    goldIngot14(count)
    goldDust(count)

def goldIngot14(count):
    goldIngot12(count)
    goldDust(count)

def goldIngot12(count):
    goldIngot10(count)
    goldDust(count)

def goldIngot10(count):
    goldIngot8(count)
    goldDust(count)

def goldIngot8(count):
    goldIngot6(count)
    goldDust(count)

def goldIngot6(count):
    goldIngot4(count)
    goldDust(count)

def goldIngot4(count):
    goldDust(count)

def bigEnergyCapacitor(count):
    steelIngot(count*4)
    redstone(count*2)
    redstoneAlloyIngot(count*2)
    mediumEnergyCapacitor(count)

def mediumEnergyCapacitor(count):
    billionIngot(count*4)
    redstone(count*2)
    redstoneAlloyIngot(count*2)
    smallEnergyCapacitor(count)

def billionIngot(count):
    silverIngot(count)
    silverDust(count)
    copperDust(count)

def smallEnergyCapacitor(count):
    redstone(count)
    redstoneAlloyIngot(count*2)
    duraluminIngot(count*4)
    sulfate(count)
    energyConnector(count)

def sulfate(count):
    netherrack(count*16)

def energyConnector(count):
    carbon((count/8.0)*4)
    copperWire((count/8.0)*4)
    redstoneBlock((count/8.0))

def redstoneAlloyIngot(count):
    redstone(count)
    redstoneBlock(count)
    ferrosilicion(count)
    hardenedMetal(count)

def hardenedMetal(count):
    compressedCarbon(count)
    duraluminIngot(count)
    damascusSteelIngot(count)
    aluminumBronzeIngot(count)

def aluminumBronzeIngot(count):
    aluminumIngot(count)
    aluminumDust(count)
    bronzeIngot(count)

def bronzeIngot(count):
    copperIngot(count)
    copperDust(count)
    tinDust(count)

def damascusSteelIngot(count):
    carbon(count)
    ironDust(count)
    ironIngot(count)
    steelIngot(count)

def steelIngot(count):
    ironIngot(count)
    ironDust(count)
    carbon(count)

def duraluminIngot(count):
    aluminumIngot(count)
    copperDust(count)
    aluminumDust(count)

def compressedCarbon(count):
    carbon(count*4)

def ferrosilicion(count):
    silicion(count)
    ironDust(count)
    ironIngot(count)

def silicion(count):
    blockOfQuartz(count)

def blockOfQuartz(count):
    netherQuartz(count*4)

def redstoneBlock(count):
    redstone(count*9)

def opticGlass(count):
    glass(count)
    syntheticEmeraldShard(count/8.0)

def opticCable(count):
    opticGlass((count/16.0)*6.0)
    copperWire((count/16.0)*2.0)
    syntheticEmeraldShard(count/16.0)

def syntheticEmeraldShard(count):
    syntheticEmerald((count/3.0)*2.0)
    stoneChunk((count/3.0))

def syntheticEmerald(count):
    aluminumIngot(count)
    aluminumDust(count)
    syntheticSapphire(count)
    glassPane(count)

def syntheticSapphire(count):
    lapisLazuli(count)
    aluminumIngot(count)
    aluminumDust(count)
    glass(count)
    glassPane(count)

def glassPane(count):
    glass((count/16.0)*6.0)

def aluminumIngot(count):
    aluminumDust(count)

def copperWire(count):
    copperIngot((count/8.0)*3)

def carbon(count):
    coal(count*8)
    try:
        cost_1["carbon"] += count
    except KeyError:
        cost_1["carbon"] = count

#  Copyright 2023 Macauley Lim xmachd@gmail.com
#  This code is licensed under GNU AFFERO GENERAL PUBLIC LICENSE v3.0.
#  A copy of this license should have been provided with the code download, if not see https://www.gnu.org/licenses/
#  This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
#  warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU AGPL v3.0 for more details.

#Raw Ingredients
def flint(count):
    global cost
    try:
        cost["flint"] += count
    except KeyError:
        cost["flint"] = count
def goldDust(count):
    global cost
    try:
        cost["gold_dust"] += count
    except KeyError:
        cost["gold_dust"] = count
def netherrack(count):
    global cost
    try:
        cost["netherrack"] += count
    except KeyError:
        cost["netherrack"] = count
def tinDust(count):
    global cost
    try:
        cost["tin_dust"] += count
    except KeyError:
        cost["tin_dust"] = count
def copperDust(count):
    global cost
    try:
        cost["copper_dust"] += count
    except KeyError:
        cost["copper_dust"] = count
def copperIngot(count):
    global cost
    try:
        cost["copper_ingot"] += count
    except KeyError:
        cost["copper_ingot"] = count
def silverDust(count):
    global cost
    try:
        cost["silver_dust"] += count
    except KeyError:
        cost["silver_dust"] = count
def silverIngot(count):
    global cost
    try:
        cost["silver_ingot"] += count
    except KeyError:
        cost["silver_ingot"] = count
def leadDust(count):
    global cost
    try:
        cost["lead_dust"] += count
    except KeyError:
        cost["lead_dust"] = count
def leadIngot(count):
    global cost
    try:
        cost["lead_ingot"] += count
    except KeyError:
        cost["lead_ingot"] = count
def netherQuartz(count):
    global cost
    try:
        cost["nether_quartz"] += count
    except KeyError:
        cost["nether_quartz"] = count
def ironDust(count):
    global cost
    try:
        cost["iron_dust"] += count
    except KeyError:
        cost["iron_dust"] = count
def ironIngot(count):
    global cost
    try:
        cost["iron_ingot"] += count
    except KeyError:
        cost["iron_ingot"] = count
def redstone(count):
    global cost
    try:
        cost["redstone"] += count
    except KeyError:
        cost["redstone"] = count
def coal(count):
    global cost
    try:
        cost["coal"] += count
    except KeyError:
        cost["coal"] = count
def aluminumDust(count):
    global cost
    try:
        cost["aluminum_dust"] += count
    except KeyError:
        cost["aluminum_dust"] = count
def glass(count):
    global cost
    try:
        cost["glass"] += count
    except KeyError:
        cost["glass"] = count
def lapisLazuli(count):
    global cost
    try:
        cost["lapis_lazuli"] += count
    except KeyError:
        cost["lapis_lazuli"] = count
def stoneChunk(count):
    global cost
    try:
        cost["stone_chunk"] += count
    except KeyError:
        cost["stone_chunk"] = count