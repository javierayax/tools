mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    describe = arcpy.Describe(layer)
    sr = describe.spatialReference
    print sr.name
