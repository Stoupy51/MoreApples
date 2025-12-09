
#> more_apples:v1.3.0/load/confirm_load
#
# @within	more_apples:v1.3.0/load/secondary
#

# Confirm load
tellraw @a[tag=convention.debug] {"text":"[Loaded MoreApples v1.3.0]","color":"green"}
scoreboard players set #more_apples.loaded load.status 1

