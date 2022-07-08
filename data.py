#version 1.0.0
#https://github.com/jippie13/Keukeiland

""" read() info
GLOBAL: returns False if an error occurs
DEPENDENCIES: optional: ast.literal_eval()
WARNING: when literal_eval from the ast library is unavailable, untrusted code can be run from file!
read(<file>) will return True if file exists and can be read
read(<file>,<key>) will return the value of the key in the file
read(<file>,dict = True) will return the contents of the file as a dictionary
read(<file>,literal = True) will return the full contents of the file
"""
def read(file, key = None, literal = False, dict = False):
    try:
        fileHandle = open(file, 'rt')
    except:
        return False
    else:
        content = fileHandle.read()

        if literal == True:
            fileHandle.close()
            return content
        elif key == None and dict == False:
            fileHandle.close()
            return True
        else:
            try:
                from ast import literal_eval
                contentDict = literal_eval(content)
            except:
                contentDict = eval(content)
            finally:
                if dict == True:
                    fileHandle.close()
                    return contentDict
                try:
                    data = contentDict[key]
                except:
                    return False
        fileHandle.close()
        return data

""" append() info

"""
def append(file, key, value = None):
    if value == None:
        content = read(file, literal = True)
        if content == False:
            return False
        try:
            newContent = str(content + str(key))
        except:
            return False
        out = write(file, newContent)
        return out
    else:
        content = read(file, dict = True)
        if content == False:
            check = write(file, '{}')
            if check == False:
                return False
            else:
                content = read(file, dict = True)
        content.update({key:value})
        out = write(file, str(content))
        return out

""" write() info#
"""
def write(file, key = None, value = None):
    if key == None:
        try:
            fileHandle = open(file, 'xt')
            fileHandle.close()
            return True
        except:
            return False
    else:
        try:
            fileHandle = open(file, 'wt')
            if value == None:
                fileHandle.write(key)
            else:
                data = {key:value}
                fileHandle.write(str(data))
            fileHandle.close()
            return True
        except:
            return False

""" delete() info
GLOBAL: returns True if successfull, False if not
DEPENDENCIES: read(), write(), os.remove()
delete(<file>) will try to delete <file>
delete(<file>,<key>) will try to remove <key> from the dictionary in <file>
"""
def delete(file, key = None):
    if key == None:
        try:
            from os import remove
            remove(file)
            return True
        except:
            return False
    else:
        content = read(file, dict = True)
        if content == False:
            return False
        content.pop(key)
        out = write(file, str(content))
        return out
