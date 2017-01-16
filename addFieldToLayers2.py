import arcpy
mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)

for layer in layers:
    try:
        fields = [field.name for field in arcpy.ListFields(layer)]
        if 'EDITOR' not in fields:
            arcpy.AddField_management(layer, 'EDITOR', "TEXT", field_length = 50)
        arcpy.CalculateField_management(layer, field = "EDITOR", expression='"jescudero"', expression_type="PYTHON_9.3", code_block="")

        if 'EDITION_DATE' not in fields:
            arcpy.AddField_management(layer, 'EDITION_DATE', "DATE")
        arcpy.CalculateField_management(layer, field = "EDITION_DATE", expression="time.strftime('%d/%m/%Y')", expression_type="PYTHON_9.3", code_block="")
    except:
        print layer


arcpy.RefreshTOC()