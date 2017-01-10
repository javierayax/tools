import os, arcpy
mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)
workspace = r"D:\SIIMA\EstructuracionDatos\A2.gdb"

for layer in layers:
    try:
        arcpy.Project_management(layer, os.path.join(workspace, layer.name), arcpy.SpatialReference(4326))
    except:
        print layer.name

