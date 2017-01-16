mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

arcpy.env.workspace = r"D:\SIIMA\EstructuracionDatos\CIFRAS_PONAL_COCA.gdb"
layers = arcpy.ListFeatureClasses()

total = 0
for layer in layers:
    n = long(arcpy.GetCount_management(layer).getOutput(0))
    print n
    total += n
    if n == 482:
        print layer

print total


