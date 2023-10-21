def conditions(headers):
    return isvideo(headers["Content-type"])

def isvideo(type):
    return type.split("/")[0] == "video"