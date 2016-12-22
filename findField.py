mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)
campo = u'FRANJA'

for layer in layers:
    fields = [field.name for field in arcpy.ListFields(layer)]
    layer.visible = campo in fields

arcpy.RefreshTOC()