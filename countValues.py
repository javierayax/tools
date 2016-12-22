import arcpy
dicFields = {}
layer = arcpy.GetParameter(0)

fields = [field.name for field in arcpy.ListFields(layer)]
for field in fields:
    dicFields[field] = 0

n = long(arcpy.GetCount_management(layer).getOutput(0))
arcpy.SetProgressor('step', 'contando valores', 0, n, 1)
with arcpy.da.SearchCursor(layer, fields) as cursor:
    for row in cursor:
        arcpy.SetProgressorPosition()
        i = 0
        print row
        for field in fields:
            value = row[i]
            print value
            if value == None:
                dicFields[fields[i]] += 1
            i+=1

arcpy.AddMessage(dicFields)
arcpy.ResetProgressor()

