import os, arcpy
mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    layer.name = layer.name.replace("COLOMBIA_COP_VECTOR_DBO_", "")

arcpy.RefreshTOC()