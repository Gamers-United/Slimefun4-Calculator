from ingredient import Ingredient
from recipe import Recipe

# Base Ingredients (Minecraft)
oakLog = Ingredient("minecraft:oak_log", True)
flint = Ingredient("minecraft:flint", True)
cobblestone = Ingredient("minecraft:cobblestone", True)
gravel = Ingredient("minecraft:gravel", True)
sand = Ingredient("minecraft:sand", True)
ice = Ingredient("minecraft:ice", True)

redstone = Ingredient("minecraft:redstone", True)
coal = Ingredient("minecraft:coal", True)
lapisLazuli = Ingredient("minecraft:lapis_lazuli", True)
emerald = Ingredient("minecraft:emerald", True)
diamond = Ingredient("minecraft:diamond", True)

ironIngot = Ingredient("minecraft:iron_ingot", True)

gunpowder = Ingredient("minecraft:gunpowder", True)
slime = Ingredient("minecraft:slime_ball", True)
string = Ingredient("minecraft:string", True)

netherrack = Ingredient("minecraft:netherrack", True)
netherQuartz = Ingredient("minecraft:nether_quartz", True)
netherWart = Ingredient("minecraft:nether_wart", True)
netherStar = Ingredient("minecraft:nether_star", True)

soulSand = Ingredient("minecraft:soul_sand", True)

blazeRod = Ingredient("minecraft:blaze_rod", True)
magmaCream = Ingredient("minecraft:magma_cream", True)

enderPearl = Ingredient("minecraft:ender_pearl", True)

# Base Ingredients (Slimefun4)
goldDust = Ingredient("slimefun4:gold_Dust", True)

tinDust = Ingredient("slimefun4:tin_Dust", True)
tinIngot = Ingredient("slimefun4:tin_ingot", True)

zincDust = Ingredient("slimefun4:zinc_Dust", True)
zincIngot = Ingredient("slimefun4:zinc_ingot", True)

copperDust = Ingredient("slimefun4:copper_Dust", True)
copperIngot = Ingredient("slimefun4:copper_ingot", True)

silverDust = Ingredient("slimefun4:silver_Dust", True)
silverIngot = Ingredient("slimefun4:silver_ingot", True)

leadDust = Ingredient("slimefun4:lead_Dust", True)
leadIngot = Ingredient("slimefun4:lead_ingot", True)

ironDust = Ingredient("slimefun4:iron_Dust", True)

aluminumDust = Ingredient("slimefun4:aluminum_Dust", True)
aluminumIngot = Ingredient("slimefun4:aluminum_ingot", True)

magnesium = Ingredient("slimefun4:magnesium", True)

siftedOre = Ingredient("slimefun4:sifted_ore", True)
stoneChunk = Ingredient("slimefun4:stone_chunk", True)

basicBoard = Ingredient("slimefun4:basic_circuit_board", True).addAquisitionDescriptor("entity_kill", "Iron Golem")

uraniumChunk = Ingredient("slimefun4:uranium_chunk", True)
thorium = Ingredient("slimefun4:thorium", True)
netherIce = Ingredient("slimefun4:nether_ice", True)    

# Machine definitions
rclick = 'minecraft:use'
furn = 'minecraft:furnace'
crft = 'minecraft:crafting_table'
ecrft = 'slimefun4:enhanced_crafting_table'
cmprs = 'slimefun4:compressor'
pcr = 'slimefun4:pressure_chamber'
hpcr = "slimefun4:heated_pressure_chamber"
smlt = 'slimefun4:smeltery'
crsh = 'slimefun4:ore_crusher'
grnd = 'slimefun4:grind_stone'
mgic = 'slimefun4:magic_workbench'
nuke = 'slimefun4:nuclear_reactor'
wash = 'slimefun4:ore_washer'
saw = 'slimefun4:table_saw'

# Blaze Powder Grindstone Recipe or Vanilla Recipe
#blazePowder = Ingredient("minecraft:blaze_powder").addRecipe([blazeRod], 2, crft)
blazePowder = Ingredient("minecraft:blaze_powder").addRecipe([blazeRod], 4, grnd)

# Oak Plank Sawmill and Stick Recipe or Vanilla Recipe
#oakPlank = Ingredient("minecraft:oak_planks").addRecipe([oakLog], 4, crft)
oakPlank = Ingredient("minecraft:oak_planks").addRecipe([oakLog], 8, saw)
#stick = Ingredient("minecraft:stick").addRecipe([oakPlank.getQty(2)], 4, crft)
stick = Ingredient("minecraft:stick").addRecipe([oakPlank], 4, saw)

# Minecraft Recipes
glass = Ingredient("minecraft:glass").addRecipe([sand], 1, furn)
glassPane = Ingredient("minecraft:glass_pane").addShapedRecipe([[None,None,None],[glass, glass, glass],[glass, glass, glass]], 16, crft)
quartzBlock = Ingredient("minecraft:quartz_block").addShapedRecipe([[netherQuartz,netherQuartz, None],[netherQuartz, netherQuartz, None],[None, None, None]], 1, crft)
magmaBlock = Ingredient("minecraft:magma_block").addShapedRecipe([[magmaCream, magmaCream, None],[magmaCream, magmaCream, None],[None, None, None]], 1, crft)
enderEye = Ingredient("minecraft:eye_of_ender").addRecipe([blazePowder, enderPearl], 1, crft)
ironBlock = Ingredient("minecraft:iron_block").addRecipe([ironIngot.getQty(9)], 1, crft)
redstoneBlock = Ingredient("minecraft:redstone_block").addRecipe([redstone.getQty(9)], 1, crft)
lapisBlock = Ingredient("minecraft:lapis_block").addRecipe([lapisLazuli.getQty(9)], 1, crft)
slimeBlock = Ingredient("minecraft:slime_block").addRecipe([slime.getQty(9)], 1, crft)
craftingTable = Ingredient("minecraft:crafting_table").addRecipe([oakPlank.getQty(4)], 1, crft)
bow = Ingredient("minecraft:bow").addRecipe([stick.getQty(3), string.getQty(3)], 1, crft)
dispenser = Ingredient("minecraft:dispenser").addRecipe([redstone, bow, cobblestone.getQty(7)], 1, crft)

# Slimefun 4 Magic Recipes
magiclumpI = Ingredient("slimefun4:magic_lump_1").addRecipe([netherWart], 2, grnd)
magiclumpII = Ingredient("slimefun4:magic_lump_2").addShapedRecipe([[magiclumpI,magiclumpI,None],[magiclumpI,magiclumpI,None],[None,None,None]], 1, ecrft)
magiclumpIII = Ingredient("slimefun4:magic_lump_3").addShapedRecipe([[magiclumpII,magiclumpII,None],[magiclumpII,magiclumpII,None],[None,None,None]], 1, ecrft)
enderlumpI = Ingredient("slimefun4:ender_lump_1").addRecipe([enderEye], 2, grnd)
enderlumpII = Ingredient("slimefun4:ender_lump_2").addShapedRecipe([[enderlumpI,enderlumpI,None],[enderlumpI,enderlumpI,None],[None,None,None]], 1, ecrft)
enderlumpIII = Ingredient("slimefun4:ender_lump_3").addShapedRecipe([[enderlumpII,enderlumpII,None],[enderlumpII,enderlumpII,None],[None,None,None]], 1, ecrft)

# Slimefun 4 Resources
gold4k = Ingredient("slimefun4:gold_4k").addRecipe([goldDust.getQty(1)], 1, smlt)
gold6k = Ingredient("slimefun4:gold_6k").addRecipe([goldDust.getQty(2)], 1, smlt)
gold8k = Ingredient("slimefun4:gold_8k").addRecipe([goldDust.getQty(3)], 1, smlt)
gold10k = Ingredient("slimefun4:gold_10k").addRecipe([goldDust.getQty(4)], 1, smlt)
gold12k = Ingredient("slimefun4:gold_12k").addRecipe([goldDust.getQty(5)], 1, smlt)
gold14k = Ingredient("slimefun4:gold_14k").addRecipe([goldDust.getQty(6)], 1, smlt)
gold16k = Ingredient("slimefun4:gold_16k").addRecipe([goldDust.getQty(7)], 1, smlt)
gold18k = Ingredient("slimefun4:gold_18k").addRecipe([goldDust.getQty(8)], 1, smlt)
gold20k = Ingredient("slimefun4:gold_20k").addRecipe([goldDust.getQty(9)], 1, smlt)
gold22k = Ingredient("slimefun4:gold_22k").addRecipe([goldDust.getQty(10)], 1, smlt)
gold24k = Ingredient("slimefun4:gold_24k").addRecipe([goldDust.getQty(11)], 1, smlt)
gildedIron = Ingredient("slimefun4:gilded_iron").addRecipe([gold24k, ironDust], 1, smlt)
silicon = Ingredient("slimefun4:silicon").addRecipe([quartzBlock], 1, smlt)
sulfate = Ingredient("slimefun4:sulfate").addRecipe([magmaBlock], 1, crsh)
salt = Ingredient("slimefun4:salt").addRecipe([sand], 1, wash)

# Slimefun 4 Magical Items
commonTalisman = Ingredient("slimefun4:common_talisman").addShapedRecipe([[magiclumpII, gold8k, magiclumpII],[None, emerald, None],[magiclumpII, gold8k, magiclumpII]], 1, mgic)

# Slimefun 4 Carbon Recipes
carbon = Ingredient("slimefun4:carbon").addRecipe([coal.getQty(8)], 1, cmprs)
compressedCarbon = Ingredient("slimefun4:compressed_carbon").addRecipe([carbon.getQty(4)], 1, cmprs)
carbonChunk = Ingredient("slimefun4:carbon_chunk").addShapedRecipe([[compressedCarbon, compressedCarbon, compressedCarbon], [compressedCarbon, flint, compressedCarbon], [compressedCarbon, compressedCarbon, compressedCarbon]], 1, ecrft)
synthDiamond = Ingredient("slimefun4:synthetic_diamond").addRecipe([carbonChunk], 1, pcr)
rawCarbonado = Ingredient("slimefun4:raw_carbonado").addRecipe([synthDiamond,carbonChunk, glassPane], 1, pcr)
carbonado = Ingredient("slimefun4:carbonado").addRecipe([rawCarbonado], 1, pcr)
synthSapphire = Ingredient("slimefun4:synthetic_sapphire").addRecipe([aluminumIngot, aluminumDust, glass, glassPane, lapisLazuli], 1, smlt)
synthEmerald = Ingredient("slimefun4:synthetic_sapphire").addRecipe([synthSapphire, aluminumIngot, aluminumDust, glassPane], 1, smlt)

# Slimefun 4 Alloys
nickelIngot = Ingredient("slimefun4:nickel_ingot").addRecipe([ironDust, ironIngot, copperDust], 1, smlt)
cobaltIngot = Ingredient("slimefun4:cobalt_ingot").addRecipe([ironDust, nickelIngot, copperDust], 1, smlt)
ferrosilicon = Ingredient("slimefun4:ferrosilicon").addRecipe([ironIngot, ironDust, silicon], 1, smlt)
solderIngot = Ingredient("slimefun4:solder_ingot").addRecipe([leadIngot, leadDust, tinDust], 1, smlt)
billonIngot = Ingredient("slimefun4:billon_ingot").addRecipe([silverIngot, silverDust, copperDust], 1, smlt)
bronzeIngot = Ingredient("slimefun4:bronze_ingot").addRecipe([copperIngot, copperDust, tinDust], 1, smlt)
corinthianBronzeIngot = Ingredient("slimefun4:corinthian_bronze_ingot").addRecipe([bronzeIngot, goldDust, silverDust, copperDust], 1, smlt)
aluminumBronzeIngot = Ingredient("slimefun4:aluminum_bronze_ingot").addRecipe([bronzeIngot, aluminumIngot, aluminumDust], 1, smlt)
duraluminIngot = Ingredient("slimefun4:duralumin_ingot").addRecipe([aluminumIngot, aluminumDust, copperDust], 1, smlt)
steelIngot = Ingredient("slimefun4:steel_ingot").addRecipe([ironIngot, ironDust, carbon], 1, smlt)
steelPlate = Ingredient("slimefun4:steel_plate").addRecipe([steelIngot.getQty(8)], 1, cmprs)
damascusSteelIngot = Ingredient("slimefun4:damascus_steel_ingot").addRecipe([steelIngot, ironIngot, ironDust, carbon], 1, smlt)
hardenedMetal = Ingredient("slimefun4:hardened_metal_ingot").addRecipe([compressedCarbon, duraluminIngot, damascusSteelIngot, aluminumBronzeIngot], 1, smlt)
reinforcedAlloyIngot = Ingredient("slimefun4:reinforced_alloy_ingot").addRecipe([damascusSteelIngot, hardenedMetal, corinthianBronzeIngot, solderIngot, billonIngot, gold24k], 1, smlt)
redstoneAlloyIngot = Ingredient("slimefun4:redstone_alloy").addRecipe([hardenedMetal, ferrosilicon, redstoneBlock, redstone], 1, smlt)
reinforcedPlate = Ingredient("slimefun4:reinforced_plate").addRecipe([reinforcedAlloyIngot.getQty(8)], 1, cmprs)
magnesiumSalt = Ingredient("slimefun4:magnesium_salt").addRecipe([magnesium, salt], 1, hpcr)

# Slimefun 4 Technical Components
advancedCircuitBoard = Ingredient("slimefun4:advanced_circuit_board").addShapedRecipe([[lapisBlock, lapisBlock, lapisBlock],[redstoneBlock, basicBoard, redstoneBlock],[lapisBlock, lapisBlock, lapisBlock]], 1, ecrft)
magnet = Ingredient("slimefun4:magnet").addRecipe([nickelIngot, cobaltIngot, aluminumDust, copperDust], 1, smlt)
battery = Ingredient("slimefun4:battery").addShapedRecipe([redstone, zincIngot.getQty(2), copperIngot.getQty(2), sulfate.getQty(2)], 1, [[None, redstone, None],[zincIngot, sulfate, copperIngot],[zincIngot, sulfate, copperIngot]], ecrft)
electroMagnet = Ingredient("slimefun4:electro_magnet").addShapedRecipe([nickelIngot, magnet, cobaltIngot, battery], 1, [[nickelIngot, magnet, cobaltIngot],[None, battery, None],[None, None, None]], ecrft)
copperWire = Ingredient("slimefun4:copper_wire").addShapedRecipe([[None,None,None],[copperIngot, copperIngot, copperIngot],[None,None,None]], 8, ecrft)
electricMotor = Ingredient("slimefun4:electric_motor").addShapedRecipe([[copperWire, copperWire, copperWire],[None, electroMagnet, None],[copperWire, copperWire, copperWire]], 1, ecrft)
heatingCoil = Ingredient("slimefun4:heating_coil").addShapedRecipe([[copperWire, copperWire, copperWire],[copperWire, electroMagnet, copperWire],[copperWire, copperWire, copperWire]], 1, ecrft)
powerCrystal = Ingredient("slimefun4:power_crystal").addRecipe([synthDiamond, synthSapphire.getQty(4), redstone.getQty(4)], 1, ecrft)
hardenedGlass = Ingredient("slimefun4:hardened_glass").addRecipe([reinforcedPlate, glass.getQty(8)], 16, ecrft)
coolingUnit = Ingredient("slimefun4:cooling_unit").addRecipe([electricMotor, aluminumIngot.getQty(2), ice.getQty(6)], 1, ecrft)

# Slimefun 4 Energy
energyConnector = Ingredient("slimefun4:energy_connector").addRecipe([redstoneBlock, copperWire.getQty(4), carbon.getQty(4)], 8, ecrft)
smallCap = Ingredient("slimefun4:cooling_unit").addRecipe([electricMotor, aluminumIngot.getQty(2), ice.getQty(6)], 16, ecrft)

# Slimefun 4 Radioactive Recipes
uranium = Ingredient("slimefun4:uranium").addShapedRecipe([[uraniumChunk, uraniumChunk, None],[uraniumChunk, uraniumChunk, None],[None, None, None]], 1, ecrft)
neptunium = Ingredient("slimefun4:neptunium").addRecipe([uranium], 1, nuke)
plutonium  = Ingredient("slimefun4:plutonium").addRecipe([neptunium], 1, nuke)
boostedUranium = Ingredient("slimefun4:boosted_uranium").addRecipe([plutonium, uranium], 1, hpcr)
enrichedNetherIce = Ingredient("slimefun4:enriched_nether_ice").addRecipe([netherIce, plutonium], 4, hpcr)
blisteringIngot1 = Ingredient("slimefun4:blistering_ingot_1").addRecipe([uranium, gold24k], 1, hpcr)
blisteringIngot2 = Ingredient("slimefun4:blistering_ingot_2").addRecipe([blisteringIngot1, carbonado], 1, hpcr)
blisteringIngot3 = Ingredient("slimefun4:blistering_ingot_3").addRecipe([blisteringIngot2, netherStar], 1, hpcr)

# Slimefun 4 Cargo Management
cargoMotor = Ingredient("slimefun4:cargo_motor").addRecipe([electricMotor, silverIngot.getQty(2), electroMagnet.getQty(2), hardenedGlass.getQty(4)], 4, ecrft)
cargoNode = Ingredient("slimefun4:cargo_node").addRecipe([cargoMotor, silverIngot.getQty(4), bronzeIngot.getQty(4)], 4, ecrft)
craftingMotor = Ingredient("slimefun4:crafting_motor").addRecipe([cargoMotor, redstoneAlloyIngot.getQty(2), blisteringIngot3.getQty(2), craftingTable.getQty(4)], 2, ecrft)
vanillaAutoCrafter = Ingredient("slimefun4:vanilla_auto_crafter").addRecipe([cargoMotor, craftingMotor, electricMotor, craftingTable.getQty(2)], 1, ecrft)
enhancedAutoCrafter = Ingredient("slimefun4:enhanced_auto_crafter").addRecipe([craftingMotor, dispenser, cargoMotor, craftingTable.getQty(2)], 1, ecrft)


#Addon Slimefun Warfare
slimeSteel = Ingredient("slimefun4:slimesteel_ingot").addRecipe([steelIngot, slime], 1, smlt)
reinforcedSlimeSteel = Ingredient("slimefun4:reinforced_slimesteel_ingot").addRecipe([slimeSteel, slimeBlock, damascusSteelIngot, hardenedMetal, corinthianBronzeIngot, aluminumBronzeIngot], 1, smlt)

# Addon Networks
synthEmeraldShard = Ingredient("slimefun4:ntw_synthetic_emerald_shard").addShapedRecipe([[stoneChunk, synthEmerald, None],[synthEmerald,None,None],[None,None,None]], 3, ecrft)
opticGlass = Ingredient("slimefun4:ntw_optic_glass").addRecipe([synthEmeraldShard, glass.getQty(8)], 8, ecrft)
opticCable = Ingredient("slimefun4:ntw_optic_cable").addRecipe([synthEmeraldShard, copperWire.getQty(2), opticGlass.getQty(6)], 16, ecrft)
opticStar = Ingredient("slimefun4:ntw_optic_star").addRecipe([netherStar, opticCable.getQty(4), opticGlass.getQty(4)], 1, ecrft)
radOpticStar = Ingredient("slimefun4:ntw_radioactice_optic_star").addRecipe([opticStar, opticCable.getQty(2), blisteringIngot3.getQty(6)], 1, ecrft)
networkBridge = Ingredient("slimefun4:ntw_bridge").addRecipe([cargoNode, opticCable.getQty(4), opticGlass.getQty(4)], 1, ecrft)

# Addon Missile Warfare
explosivepowder = Ingredient("slimefun4:explosivepowder").addShapedRecipe([[magnesium, coal, magnesium],[coal, gunpowder, coal],[magnesium, coal, magnesium]], 1, ecrft)
compressedexplosives = Ingredient("slimefun4:compressedexplosives").addShapedRecipe([[None, gunpowder, None],[explosivepowder, explosivepowder, explosivepowder],[None, gunpowder, None]], 1, ecrft)
rocketfuel = Ingredient("slimefun4:rocketfuel").addShapedRecipe([[explosivepowder, gunpowder, explosivepowder],[None, aluminumDust, None],[explosivepowder, gunpowder, explosivepowder]], 1, ecrft)
