mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

#arcpy.env.workspace = r"D:\SIIMA\EstructuracionDatos\folder1\gdb1.gdb"
#layers = arcpy.ListFeatureClasses()

for layer in layers:
    describe = arcpy.Describe(layer)
    sr = describe.spatialReference
    print describe.extent.XMin
    print sr.name
