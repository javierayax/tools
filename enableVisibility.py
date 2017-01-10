import arcpy
mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)


for layer in layers:
  if arcpy.Describe(layer).spatialReference.name != u'GCS_WGS_1984':
    if abs(arcpy.Describe(layer).extent.XMin) > 0 and abs(arcpy.Describe(layer).extent.XMin) < 180:
      layer.visible = 1

for layer in layers:
    if abs(arcpy.Describe(layer).extent.XMin) > 0 and abs(arcpy.Describe(layer).extent.XMin) < 180:
      layer.visible = 1
      print arcpy.Describe(layer).spatialReference.name

for layer in layers:
    arcpy.DefineProjection_management(layer, arcpy.SpatialReference(4326))

arcpy.RefreshTOC()