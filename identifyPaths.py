mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    path = layer.dataSource
    paths += path + ";"

paths = paths[:-1]

