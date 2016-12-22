mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)
  
total = 0
for layer in layers:
    n = long(arcpy.GetCount_management(layer).getOutput(0))
    print n 
    total += n

print total

 
