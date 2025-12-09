
#> more_apples:v1.3.0/load/enumerate
#
# @within	#more_apples:enumerate
#

# If current major is too low, set it to the current major
execute unless score #more_apples.major load.status matches 1.. run scoreboard players set #more_apples.major load.status 1

# If current minor is too low, set it to the current minor (only if major is correct)
execute if score #more_apples.major load.status matches 1 unless score #more_apples.minor load.status matches 3.. run scoreboard players set #more_apples.minor load.status 3

# If current patch is too low, set it to the current patch (only if major and minor are correct)
execute if score #more_apples.major load.status matches 1 if score #more_apples.minor load.status matches 3 unless score #more_apples.patch load.status matches 0.. run scoreboard players set #more_apples.patch load.status 0

