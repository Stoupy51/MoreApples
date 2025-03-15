
# Imports
import stouputils as stp
from python_datapack.constants import *
from python_datapack.utils.io import *
from config import *
import requests

# Main function is run just before making finalyzing the build process (zip, headers, lang, ...)
def main(config: dict) -> None:
	MULTIPLIER: int = 2
	loot_tables_path: str = f"{config['build_datapack']}/data/minecraft/loot_table/blocks"
	minecraft_default_data: str = "https://raw.githubusercontent.com/PixiGeko/Minecraft-default-data/latest/data/minecraft/loot_table/blocks"
	leaves: dict[str, dict] = {
		"acacia" : {},
		"azalea" : {},
		"birch": {},
		"cherry": {},
		"dark_oak": {},
		"flowering_azalea": {},
		"jungle": {},
		"mangrove": {},
		"oak": {},
		"spruce": {},
		"pale_oak": {},
	}

	# Download all loot tables
	for leave in leaves.keys():
		leaves[leave] = requests.get(f"{minecraft_default_data}/{leave}_leaves.json").json()

	# Get the multiplied pool from oak_leaves.json
	apple_pool = [pool for pool in leaves["oak"]["pools"] if pool["entries"][0].get("name") == "minecraft:apple"][0]
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
		write_to_file(f"{loot_tables_path}/{leave}_leaves.json", stp.super_json_dump(loot_table, max_level = -1))

