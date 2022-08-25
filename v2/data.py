from ingredient import Ingredient
from recipe import Recipe

# Base Ingredients (Minecraft)
flint = Ingredient("minecraft:flint", True)
gravel = Ingredient("minecraft:gravel", True)
sand = Ingredient("minecraft:sand", True)

redstone = Ingredient("minecraft:redstone", True)
coal = Ingredient("minecraft:coal", True)
lapislazuli = Ingredient("minecraft:lapis_lazuli", True)
ironIngot = Ingredient("minecraft:iron_ingot", True)

gunpowder = Ingredient("minecraft:gunpowder", True)

netherrack = Ingredient("minecraft:netherrack", True)
netherquartz = Ingredient("minecraft:nether_quartz", True)
netherwart = Ingredient("minecraft:nether_wart", True)
netherstar = Ingredient("minecraft:nether_star", True)

blaze_rod = Ingredient("minecraft:blaze_rod", True)
magma_cream = Ingredient("minecraft:magma_cream", True)

enderpearl = Ingredient("minecraft:ender_pearl", True)

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

stonechunk = Ingredient("slimefun4:stone_chunk", True)

basicBoard = Ingredient("slimefun4:basic_circuit_board", True)

uranium_chunk = Ingredient("slimefun4:uranium_chunk", True)
thorium = Ingredient("slimefun4:thorium", True)
netherice = Ingredient("slimefun4:nether_ice", True)

# Machine definitions
rclick = 'minecraft:use'
furn = 'minecraft:furnace'
crft = 'minecraft:crafting_table'
ecrft = 'slimefun4:enhanced_crafting_table'
compr = 'slimefun4:compressor'
pcr = 'slimefun4:pressure_chamber'
hpcr = "slimefun4:heated_pressure_chamber"
smlt = 'slimefun4:smeltery'
crsh = 'slimefun4:ore_crusher'
grnd = 'slimefun4:grind_stone'
mgic = 'slimefun4:magic_workbench'
nuke = 'slimefun4:nuclear_reactor'
wash = 'slimefun4:ore_washer'

# Blaze Powder Grindstone Recipe or Vanilla Recipe
#blaze_powder = Ingredient("minecraft:blaze_powder").addRecipe([blaze_rod], 2, crft)
blaze_powder = Ingredient("minecraft:blaze_powder").addRecipe([blaze_rod], 4, grnd)

# Minecraft Recipes
glass = Ingredient("minecraft:glass").addRecipe([sand], 1, furn)
glassPane = Ingredient("minecraft:glass_pane").addShapedRecipe([glass.getQty(6)], 16, [[None,None,None],[glass, glass, glass],[glass, glass, glass]], crft)
quartz_block = Ingredient("minecraft:quartz_block").addShapedRecipe([netherquartz.getQty(4)], 1, [[netherquartz,netherquartz, None],[netherquartz, netherquartz, None],[None, None, None]], crft)
magma_block = Ingredient("minecraft:magma_block").addShapedRecipe([magma_cream.getQty(4)], 1, [[magma_cream, magma_cream, None],[magma_cream, magma_cream, None],[None, None, None]], crft)
endereye = Ingredient("minecraft:eye_of_ender").addRecipe([blaze_powder, enderpearl], 1, crft)
redstoneBlock = Ingredient("minecraft:redstone_block").addRecipe([redstone.getQty(9)], 1, crft)
lapisBlock = Ingredient("minecraft:lapis_block").addRecipe([lapislazuli.getQty(9)], 1, crft)

# Slimefun 4 Magic Recipes
magiclumpI = Ingredient("slimefun4:magic_lump_1").addRecipe([netherwart], 2, grnd)
magiclumpII = Ingredient("slimefun4:magic_lump_2").addShapedRecipe([magiclumpI.getQty(4)], 1, [[magiclumpI,magiclumpI,None],[magiclumpI,magiclumpI,None],[None,None,None]], ecrft)
magiclumpIII = Ingredient("slimefun4:magic_lump_3").addShapedRecipe([magiclumpII.getQty(4)], 1, [[magiclumpII,magiclumpII,None],[magiclumpII,magiclumpII,None],[None,None,None]], ecrft)
enderlumpI = Ingredient("slimefun4:ender_lump_1").addRecipe([endereye], 2, grnd)
enderlumpII = Ingredient("slimefun4:ender_lump_2").addShapedRecipe([enderlumpI.getQty(4)], 1, [[enderlumpI,enderlumpI,None],[enderlumpI,enderlumpI,None],[None,None,None]], ecrft)
enderlumpIII = Ingredient("slimefun4:ender_lump_3").addShapedRecipe([enderlumpII.getQty(4)], 1, [[enderlumpII,enderlumpII,None],[enderlumpII,enderlumpII,None],[None,None,None]], ecrft)

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
silicon = Ingredient("slimefun4:silicon").addRecipe([quartz_block], 1, smlt)
sulfate = Ingredient("slimefun4:sulfate").addRecipe([magma_block], 1, crsh)
salt = Ingredient("slimefun4:salt").addRecipe([sand], 1, wash)

# Slimefun 4 Carbon Recipes
carbon = Ingredient("slimefun4:carbon").addRecipe([coal.getQty(8)], 1, compr)
compressedCarbon = Ingredient("slimefun4:compressedCarbon").addRecipe([carbon.getQty(4)], 1, compr)
carbon_chunk = Ingredient("slimefun4:carbon_chunk").addShapedRecipe([compressedCarbon.getQty(8),flint], 1, [[compressedCarbon, compressedCarbon, compressedCarbon], [compressedCarbon, flint, compressedCarbon], [compressedCarbon, compressedCarbon, compressedCarbon]], ecrft)
synthetic_diamond = Ingredient("slimefun4:synthetic_diamond").addRecipe([carbon_chunk], 1, pcr)
raw_carbonado = Ingredient("slimefun4:raw_carbonado").addRecipe([synthetic_diamond,carbon_chunk, glassPane], 1, pcr)
carbonado = Ingredient("slimefun4:carbonado").addRecipe([raw_carbonado], 1, pcr)
synthetic_sapphire = Ingredient("slimefun4:synthetic_sapphire").addRecipe([aluminumIngot, aluminumDust, glass, glassPane, lapislazuli], 1, smlt)
synthetic_emerald = Ingredient("slimefun4:synthetic_sapphire").addRecipe([synthetic_sapphire, aluminumIngot, aluminumDust, glassPane], 1, smlt)

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
steelPlate = Ingredient("slimefun4:steel_plate").addRecipe([steelIngot.getQty(8)], 1, compr)
damascusSteelIngot = Ingredient("slimefun4:damascus_steel_ingot").addRecipe([steelIngot, ironIngot, ironDust, carbon], 1, smlt)
hardenedMetal = Ingredient("slimefun4:hardened_metal_ingot").addRecipe([compressedCarbon, duraluminIngot, damascusSteelIngot, aluminumBronzeIngot], 1, smlt)
reinforcedAlloyIngot = Ingredient("slimefun4:reinforced_alloy_ingot").addRecipe([damascusSteelIngot, hardenedMetal, corinthianBronzeIngot, solderIngot, billonIngot, gold24k], 1, smlt)
redstoneAlloyIngot = Ingredient("slimefun4:redstone_alloy").addRecipe([hardenedMetal, ferrosilicon, redstoneBlock, redstone], 1, smlt)
reinforcedPlate = Ingredient("slimefun4:reinforced_plate").addRecipe([reinforcedAlloyIngot.getQty(8)], 1, compr)
magnesiumSalt = Ingredient("slimefun4:magnesium_salt").addRecipe([magnesium, salt], 1, hpcr)

# Slimefun 4 Technical Components
advancedCircuitBoard = Ingredient("slimefun4:advanced_circuit_board").addShapedRecipe([basicBoard, redstoneBlock.getQty(2), lapisBlock.getQty(6)], 1, [[lapisBlock, lapisBlock, lapisBlock],[redstoneBlock, basicBoard, redstoneBlock],[lapisBlock, lapisBlock, lapisBlock]], ecrft)
magnet = Ingredient("slimefun4:magnet").addRecipe([nickelIngot, cobaltIngot, aluminumDust, copperDust], 1, smlt)
battery = Ingredient("slimefun4:battery").addShapedRecipe([redstone, zincIngot.getQty(2), copperIngot.getQty(2), sulfate.getQty(2)], 1, [[None, redstone, None],[zincIngot, sulfate, copperIngot],[zincIngot, sulfate, copperIngot]], ecrft)
electroMagnet = Ingredient("slimefun4:electro_magnet").addShapedRecipe([nickelIngot, magnet, cobaltIngot, battery], 1, [[nickelIngot, magnet, cobaltIngot],[None, battery, None],[None, None, None]], ecrft)
copperwire = Ingredient("slimefun4:copper_wire").addShapedRecipe([glass.getQty(6)], 8, [[None,None,None],[copperIngot, copperIngot, copperIngot],[None,None,None]], ecrft)
electricMotor = Ingredient("slimefun4:electric_motor").addShapedRecipe([magnet, copperwire.getQty(6)], 1, [[copperwire, copperwire, copperwire],[None, electroMagnet, None],[copperwire, copperwire, copperwire]], ecrft)
heatingCoil = Ingredient("slimefun4:heating_coil").addShapedRecipe([electricMotor, copperwire.getQty(8)], 1, [[copperwire, copperwire, copperwire],[copperwire, electroMagnet, copperwire],[copperwire, copperwire, copperwire]], ecrft)

# Slimefun 4 Radioactive Recipes
uranium = Ingredient("slimefun4:uranium").addShapedRecipe([uranium_chunk.getQty(4)], 1, [[uranium_chunk, uranium_chunk, None],[uranium_chunk, uranium_chunk, None],[None, None, None]], ecrft)
neptunium = Ingredient("slimefun4:neptunium").addRecipe([uranium], 1, nuke)
plutonium  = Ingredient("slimefun4:plutonium").addRecipe([neptunium], 1, nuke)
boostedUranium = Ingredient("slimefun4:boosted_uranium").addRecipe([plutonium, uranium], 1, hpcr)
enrichedNetherIce = Ingredient("slimefun4:enriched_nether_ice").addRecipe([netherice, plutonium], 4, hpcr)
blisteringIngot1 = Ingredient("slimefun4:blistering_ingot_1").addRecipe([uranium, gold24k], 1, hpcr)
blisteringIngot2 = Ingredient("slimefun4:blistering_ingot_2").addRecipe([blisteringIngot1, carbonado], 1, hpcr)
blisteringIngot3 = Ingredient("slimefun4:blistering_ingot_3").addRecipe([blisteringIngot2, netherstar], 1, hpcr)

# Addon Missile Warfare
explosivepowder = Ingredient("slimefun4:explosivepowder").addShapedRecipe([gunpowder, magnesium.getQty(4), coal.getQty(4)], 1, [[magnesium, coal, magnesium],[coal, gunpowder, coal],[magnesium, coal, magnesium]], ecrft)
compressedexplosives = Ingredient("slimefun4:compressedexplosives").addShapedRecipe([gunpowder.getQty(2), explosivepowder.getQty(3)], 1, [[None, gunpowder, None],[explosivepowder, explosivepowder, explosivepowder],[None, gunpowder, None]], ecrft)
rocketfuel = Ingredient("slimefun4:rocketfuel").addShapedRecipe([aluminumDust, gunpowder.getQty(2), explosivepowder.getQty(4)], 1, [[explosivepowder, gunpowder, explosivepowder],[None, aluminumDust, None],[explosivepowder, gunpowder, explosivepowder]], ecrft)