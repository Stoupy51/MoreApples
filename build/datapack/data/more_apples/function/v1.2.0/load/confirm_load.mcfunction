
#> more_apples:v1.2.0/load/confirm_load
#
# @within	more_apples:v1.2.0/load/secondary
#

tellraw @a[tag=convention.debug] {"text":"[Loaded More Apples v1.2.0]","color":"green"}

scoreboard players set #more_apples.loaded load.status 1

