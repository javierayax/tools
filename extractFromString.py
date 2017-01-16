import arcpy
def extract(string, sep, position):
    try:
        return string.split(sep)[position]
    except:
        return None

