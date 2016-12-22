import os, arcpy
folder = r"Z:\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo"
x = 0

capas = []
for root, dirs, files in os.walk(folder):
    for file in files:
        desc = arcpy.Describe(os.path.join(root, file))
        if desc.dataType == u'ShapeFile':
             x += 1
             #arcpy.MakeFeatureLayer_management(desc.catalogPath)
             sr = desc.spatialReference
             try:
                 print "%s-%s-%s-%s" %  (sr.name,  desc.extent.XMin, desc.extent.XMax, x)
                 capas.append(file)
             except:
                print file


workspace = r"D:\SIIMA\EstructuracionDatos\LINEASVUELO.gdb"
for capa in capas:
    try:
        output = arcpy.FeatureClassToFeatureClass_conversion(r'%s' % capa, r'%s' % workspace, arcpy.ValidateTableName(arcpy.Describe(capa).name))
        arcpy.AddField_management(output, 'DATA_SOURCE', "TEXT", field_length = 500)
        arcpy.CalculateField_management(output, 'DATA_SOURCE', expression= '"%s"' % arcpy.Describe(capa).catalogPath, expression_type="VB", code_block="")
    except:
        arcpy.AddMessage("Error en capa %s" % capa)
