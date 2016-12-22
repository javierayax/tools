import arcpy
mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    arcpy.DefineProjection_management(layer, arcpy.SpatialReference(4326))

arcpy.RefreshTOC()