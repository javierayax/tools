arcpy.env.workspace = r'D:\SIIMA\EstructuracionDatos\SIIMA.gdb'
fcs = arcpy.ListFeatureClasses()
for fc in fcs:
    try:
        arcpy.Rename_management(fc, fc.upper() + "_")
        #arcpy.Rename_management(fc, fc[:-1].upper())
    except:
        print fc

tbs = arcpy.ListTables()
for tb in tbs:
    try:
        arcpy.Rename_management(tb, tb.upper() + "_")
    except:
        print tb

