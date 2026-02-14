
# Imports
from beet.contrib.vanilla import Vanilla
from stewbeet import Context, JsonDict, LootTable, set_json_encoder


# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def beet_default(ctx: Context) -> None:
	MULTIPLIER: int = 2
	leaves: dict[str, JsonDict] = {
		x: {} for x in [
			"acacia", "azalea", "birch", "cherry", "dark_oak", "flowering_azalea",
			"jungle", "mangrove", "oak", "spruce", "pale_oak"
	]}

	# Download all loot tables
	vanilla = Vanilla(ctx)
	for leave in leaves.keys():
		leaves[leave] = vanilla.data["minecraft"].loot_tables[f"blocks/{leave}_leaves"].data

	# Get the multiplied pool from oak_leaves.json
	apple_pool = next(pool for pool in leaves["oak"]["pools"] if pool["entries"][0].get("name") == "minecraft:apple")
	apple_pool["rolls"] *= MULTIPLIER

	# Modify loot tables to include apple if not present
	for leave, loot_table in leaves.items():

		# Check if the leave already has an apple pool
		has_apple: bool = False
		for pool in loot_table["pools"]:
			if pool["entries"][0].get("name") == "minecraft:apple":

				# If it does, multiply the rolls
				has_apple = True
				pool["rolls"] = apple_pool["rolls"]
				break

		# If it doesn't, add it
		if not has_apple:
			loot_table["pools"].append(apple_pool)

		# Write the json file
		ctx.data["minecraft"].loot_tables[f"blocks/{leave}_leaves"] = set_json_encoder(LootTable(loot_table), max_level=-1)

