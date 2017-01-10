import arcpy
arcpy.env.overwriteOutput =1
workspace = arcpy.GetParameterAsText(0)
capas = arcpy.GetParameterAsText(1).split(";")
for capa in capas:
    try:
        output = arcpy.TableToTable_conversion(r'%s' % capa, r'%s' % workspace, arcpy.ValidateTableName(arcpy.Describe(capa).name))
        arcpy.AddField_management(output, 'DATA_SOURCE', "TEXT", field_length = 500)
        arcpy.CalculateField_management(output, 'DATA_SOURCE', expression= '"%s"' % arcpy.Describe(capa).catalogPath, expression_type="VB", code_block="")
    except:
        arcpy.AddMessage("Error en capa %s" % capa)
