
# Imports
import os
ROOT: str = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
IGNORE_UNSET: bool = True							# If True, the program will ignore unset optionnal values in the configuration dictionnary

# Folders
BUILD_FOLDER: str = f"{ROOT}/build"					# Folder where the final datapack and resource pack are built

# Datapack related constants
AUTHOR: str = "Stoupy51"					# Author(s) name(s) displayed in pack.mcmeta, also used to add convention.debug tag to the players of the same name(s) <-- showing additionnal displays like datapack loading
DATAPACK_NAME: str = "More Apples"			# Name of the datapack, used for messages and items lore
MINECRAFT_VERSION: str = "1.21"				# Text used when loading the datapack to warn the user when the data version is not right
VERSION: str = "1.2.0"						# Datapack version in the following mandatory format: major.minor.patch, ex: 1.0.0 or 1.21.615
NAMESPACE: str = "more_apples"				# Should be the same you use in the merge folder. Used to namespace functions, tags, etc.
DATAPACK_FORMAT: int = 48					# Pack format version, see https://minecraft.wiki/w/Pack_format#List_of_data_pack_formats
DESCRIPTION = f"{DATAPACK_NAME} [{VERSION}] by {AUTHOR}"	# Pack description displayed in pack.mcmeta


# Configuration dictionnary
configuration = {
	"ignore_unset": IGNORE_UNSET,

	"build_folder": BUILD_FOLDER,
	"author": AUTHOR,
	"datapack_name": DATAPACK_NAME,
	"minecraft_version": MINECRAFT_VERSION,
	"version": VERSION,
	"namespace": NAMESPACE,
	"datapack_format": DATAPACK_FORMAT,
	"description": DESCRIPTION,
}

