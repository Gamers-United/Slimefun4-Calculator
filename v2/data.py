from ingredient import Ingredient
from recipe import Recipe

# Base Ingredients (Minecraft)
flint = Ingredient("minecraft:flint", True)
gravel = Ingredient("minecraft:gravel", True)
sand = Ingredient("minecraft:sand", True)

redstone = Ingredient("minecraft:redstone", True)
coal = Ingredient("minecraft:coal", True)
lapislazuli = Ingredient("minecraft:lapis_lazuli", True)
ironingot = Ingredient("minecraft:iron_ingot", True)

netherrack = Ingredient("minecraft:netherrack", True)
netherquartz = Ingredient("minecraft:nether_quartz", True)
nether_star = Ingredient("minecraft:nether_star", True)

blaze_rod = Ingredient("minecraft:blaze_rod", True)
magma_cream = Ingredient("minecraft:magma_cream", True)

# Base Ingredients (Slimefun4)
golddust = Ingredient("slimefun4:gold_dust", True)

tindust = Ingredient("slimefun4:tin_dust", True)
tiningot = Ingredient("slimefun4:tin_ingot", True)

copperdust = Ingredient("slimefun4:copper_dust", True)
copperingot = Ingredient("slimefun4:copper_ingot", True)

silverdust = Ingredient("slimefun4:silver_dust", True)
silveringot = Ingredient("slimefun4:silver_ingot", True)

leaddust = Ingredient("slimefun4:lead_dust", True)
leadingot = Ingredient("slimefun4:lead_ingot", True)

irondust = Ingredient("slimefun4:iron_dust", True)

aluminumdust = Ingredient("slimefun4:aluminum_dust", True)
aluminumingot = Ingredient("slimefun4:aluminum_ingot", True)

stonechunk = Ingredient("slimefun4:stone_chunk", True)

uranium_chunk = Ingredient("slimefun4:uranium_chunk", True)
thorium = Ingredient("slimefun4:thorium", True)
netherice = Ingredient("slimefun4:nether_ice", True)

furn = 'minecraft:furnace'
crft = 'minecraft:crafting_table'
ecrft = 'slimefun4:enhanced_crafting_table'
compr = 'slimefun4:compressor'
pcr = 'slimefun4:pressure_chamber'
hpcr = "slimefun4:heated_pressure_chamber"
smlt = 'slimefun4:smeltery'
crsh = 'slimefun4:ore_crusher'
grnd = 'slimefun4:grind_stone'

# Minecraft Recipes (Level 1)
glass = Ingredient("minecraft:glass").addRecipe([sand], 1, furn)
glass_pane = Ingredient("minecraft:glass_pane").addShapedRecipe([glass.getQty(6)], 16,[[],[glass, glass, glass],[glass, glass, glass]] , crft)
quartz_block = Ingredient("minecraft:quartz_block").addShapedRecipe([netherquartz.getQty(4)], 1,[[netherquartz,netherquartz],[netherquartz, netherquartz],[]] , crft)
magma_block = Ingredient("minecraft:magma_block").addShapedRecipe([magma_cream.getQty(4)], 1,[[magma_cream, magma_cream],[magma_cream, magma_cream],[]] , crft)


#Slimefun 4 Recipes (Level 1)
gold_4k = Ingredient("slimefun4:gold_4k").addRecipe([golddust.getQty(1)], 1, smlt)
gold_6k = Ingredient("slimefun4:gold_6k").addRecipe([golddust.getQty(2)], 1, smlt)
gold_8k = Ingredient("slimefun4:gold_8k").addRecipe([golddust.getQty(3)], 1, smlt)
gold_10k = Ingredient("slimefun4:gold_10k").addRecipe([golddust.getQty(4)], 1, smlt)
gold_12k = Ingredient("slimefun4:gold_12k").addRecipe([golddust.getQty(5)], 1, smlt)
gold_14k = Ingredient("slimefun4:gold_14k").addRecipe([golddust.getQty(6)], 1, smlt)
gold_16k = Ingredient("slimefun4:gold_16k").addRecipe([golddust.getQty(7)], 1, smlt)
gold_18k = Ingredient("slimefun4:gold_18k").addRecipe([golddust.getQty(8)], 1, smlt)
gold_20k = Ingredient("slimefun4:gold_20k").addRecipe([golddust.getQty(9)], 1, smlt)
gold_22k = Ingredient("slimefun4:gold_22k").addRecipe([golddust.getQty(10)], 1, smlt)
gold_24k = Ingredient("slimefun4:gold_24k").addRecipe([golddust.getQty(11)], 1, smlt)
carbon = Ingredient("slimefun4:carbon").addRecipe([coal.getQty(8)], 1, compr)
silicon = Ingredient("slimefun4:silicon").addRecipe([quartz_block], 1, smlt)
uranium = Ingredient("slimefun4:uranium").addShapedRecipe([uranium_chunk.getQty(4)], 1, [[uranium_chunk, uranium_chunk],[uranium_chunk, uranium_chunk],[]], ecrft)
sulfate = Ingredient("slimefun4:sulfate").addRecipe([magma_block], 1, crsh)
blaze_powder = Ingredient("minecraft:blaze_powder").addRecipe([blaze_rod], 4, grnd)
nickelingot = Ingredient("slimefun4:nickel_ingot", False).addRecipe([irondust, ironingot, copperdust], 1, smlt)

#Slimefun 4 Recipes (Level 2)
cobaltingot = Ingredient("slimefun4:cobalt_ingot", False).addRecipe([irondust, nickelingot, copperdust], 1, smlt)
compressed_carbon = Ingredient("slimefun4:compressed_carbon").addRecipe([carbon.getQty(4)], 1, compr)
gilded_iron = Ingredient("slimefun4:gilded_iron", False).addRecipe([gold_24k, irondust], 1, smlt)
synthetic_sapphire = Ingredient("slimefun4:synthetic_sapphire", False).addRecipe([aluminumingot, aluminumdust, glass, glass_pane, lapislazuli], 1, smlt)
synthetic_emerald = Ingredient("slimefun4:synthetic_sapphire", False).addRecipe([synthetic_sapphire, aluminumingot, aluminumdust, glass_pane], 1, smlt)

#Slimefun 4 Recipes (Level 3)
magnet = Ingredient("slimefun4:magnet", False).addRecipe([nickelingot, cobaltingot, aluminumdust, copperdust], 1, smlt)
carbon_chunk = Ingredient("slimefun4:carbon_chunk").addShapedRecipe([compressed_carbon.getQty(8),flint], 1, [[compressed_carbon, compressed_carbon, compressed_carbon], [compressed_carbon, flint, compressed_carbon], [compressed_carbon, compressed_carbon, compressed_carbon]], ecrft)
synthetic_diamond = Ingredient("slimefun4:synthetic_diamond", False).addRecipe([carbon_chunk], 1, pcr)

#Slimefun 4 Recipes (Level 4)
raw_carbonado = Ingredient("slimefun4:raw_carbonado", False).addRecipe([synthetic_diamond,carbon_chunk, glass_pane], 1, pcr)
carbonado = Ingredient("slimefun4:carbonado", False).addRecipe([raw_carbonado], 1, pcr)
blistering_ingot = Ingredient("slimefun4:blistering_ingot").addRecipe([nether_star, carbonado, uranium, gold_24k], 1, hpcr)
