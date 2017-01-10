import arcpy
arcpy.ExportGeodatabaseConfigurationKeywords_management(r'D:\SIIMA\conexiones\SDE@SIIMA01_DEV.sde', r'D:\SIIMA\Documentacion\configDBTUNE.vi')
arcpy.ImportGeodatabaseConfigurationKeywords_management(r'D:\SIIMA\conexiones\SDE@SIIMA01_DEV.sde', 'D:\\SIIMA\\Documentacion\\configDBTUNE.vi')


