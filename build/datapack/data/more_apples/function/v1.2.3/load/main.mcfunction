
#> more_apples:v1.2.3/load/main
#
# @within	more_apples:v1.2.3/load/resolve
#

# Avoiding multiple executions of the same load function
execute unless score #more_apples.loaded load.status matches 1 run function more_apples:v1.2.3/load/secondary

