mxd = arcpy.mapping.MapDocument("current")
layers = arcpy.mapping.ListLayers(mxd)


dicFields = {}
for layer in layers:
    fields = [field.name for field in arcpy.ListFields(layer)]
    for field in fields:
        if field not in dicFields.keys():
            dicFields[field] = 1
        else:
            dicFields[field] = dicFields[field] + 1

import collections
od = collections.OrderedDict(sorted(dicFields.items()))
print od
