import os, arcpy

y = 50
for folder in [r"\\172.26.179.80\sig grude\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo\2001\Del Norte NoSpray", r"\\172.26.179.80\sig grude\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo\2001\SATLOC NoSpray",
                r"\\172.26.179.80\sig grude\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo\2002\SATLOC NoSpray", r"\\172.26.179.80\sig grude\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo\2003\Del Norte NoSpray",
                r"\\172.26.179.80\sig grude\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo\2005\Del Norte NoSpray", r"\\172.26.179.80\sig grude\DATOS SIG PONAL\ASPERSIONES\lineas de vuelo\2006\Del Norte NoSpray"]:
    try:

            workspace = arcpy.CreateFolder_management(r'D:\SIIMA\EstructuracionDatos', "folder" + str(y))
            workspace2 = arcpy.CreateFileGDB_management(workspace, "gdb" + str(y))

            x = 0
            for root, dirs, files in os.walk(folder):
                for file in files:
                    desc = arcpy.Describe(os.path.join(root, file))
                    if desc.dataType == u'ShapeFile':
                        if ".shp" in file:
                             x += 1
                             sr = desc.spatialReference
                             try:
                                print "%s-%s-%s-%s" %  (sr.name,  desc.extent.XMin, desc.extent.XMax, x)
                                input = os.path.join(root, file)
                                output = arcpy.FeatureClassToFeatureClass_conversion(input, r'%s' % workspace2, arcpy.ValidateTableName(arcpy.Describe(input).name))
                                arcpy.AddField_management(output, 'DATA_SOURCE', "TEXT", field_length = 500)
                                arcpy.CalculateField_management(output, 'DATA_SOURCE', expression= '"%s"' % input, expression_type="VB", code_block="")
                             except:
                                print input
            y+=1
    except:
        print folder