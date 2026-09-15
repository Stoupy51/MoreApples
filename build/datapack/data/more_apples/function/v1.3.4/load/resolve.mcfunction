
#> more_apples:v1.3.4/load/resolve
#
# @within	#more_apples:resolve
#

# If correct version, load the datapack
execute if score #more_apples.major load.status matches 1 if score #more_apples.minor load.status matches 3 if score #more_apples.patch load.status matches 4 run function more_apples:v1.3.4/load/main

