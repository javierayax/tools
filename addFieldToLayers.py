import arcpy
mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    arcpy.AddField_management(layer, 'DATA_SOURCE', "TEXT", field_length = 500)

arcpy.RefreshTOC()