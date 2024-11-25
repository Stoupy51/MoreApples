
#> more_apples:v1.2.1/load/confirm_load
#
# @within	more_apples:v1.2.1/load/secondary
#

tellraw @a[tag=convention.debug] {"text":"[Loaded MoreApples v1.2.1]","color":"green"}

scoreboard players set #more_apples.loaded load.status 1

