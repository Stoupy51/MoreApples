
#> more_apples:v1.3.4/load/confirm_load
#
# @within	more_apples:v1.3.4/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded MoreApples v1.3.4]","color":"green"}
scoreboard players set #more_apples.loaded load.status 1
function more_apples:v1.3.4/load/set_items_storage

