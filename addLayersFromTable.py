with arcpy.da.SearchCursor("Sum_Output_2", ["DATA_SOURC"]) as cursor:
    for row in cursor:
        try:
            arcpy.MakeFeatureLayer_management(r"%s" % row[0], row[0] + "lyr")
        except:
            print row


