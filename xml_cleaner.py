import xml.etree.ElementTree as ET
from copy import deepcopy

tree = ET.parse('INPUT.xml')
root = tree.getroot()

unique_files = [] # storage for the file element.

for track in root.findall('./sequence/media/video/track'):
    for clipitem in track.findall('clipitem'):

        isUnique = False
        
        if clipitem.find('sequence') is not None:
            print ("found sequence")
            clipitem_source = clipitem.find('sequence')
            filename = clipitem.find('sequence/name') # used to check if this field has contents

        elif clipitem.find('file') is not None:
            print ("found clips")
            clipitem_source = clipitem.find('file')
            filename = clipitem.find('file/name') # used to check if this field has contents
            

        if len(unique_files) == 0: # needs to add an item first. happens once.
            unique_files.append(clipitem_source)
        else:
            for file_checking in unique_files:
                if clipitem_source.attrib['id'] == file_checking.attrib['id'] and filename is not None:
                    isUnique = False

                elif clipitem_source.attrib['id'] == file_checking.attrib['id'] and filename is None:
                    clipitem.remove(clipitem_source)
                    clipitem.append(file_checking)

                elif filename is not None:
                    isUnique = True # this means the file is NOT in the list and needs to be added

        if isUnique == True: # adds file to list
            unique_files.append(clipitem_source)
            isUnique = False

        enabled = clipitem.find('enabled')
        if (enabled.text == 'TRUE'):
            track.remove(clipitem)

# need to clean this up, there's too much duping.
for track in root.findall('./sequence/media/audio/track'):
    for clipitem in track.findall('clipitem'):

        isUnique = False
        
        if clipitem.find('sequence') is not None:
            print ("found sequence")
            clipitem_source = clipitem.find('sequence')
            filename = clipitem.find('sequence/name') # used to check if this field has contents

        elif clipitem.find('file') is not None:
            print ("found clips")
            clipitem_source = clipitem.find('file')
            filename = clipitem.find('file/name') # used to check if this field has contents
            

        if len(unique_files) == 0: # needs to add an item first. happens once.
            unique_files.append(clipitem_source)
        else:
            for file_checking in unique_files:
                if clipitem_source.attrib['id'] == file_checking.attrib['id'] and filename is not None:
                    isUnique = False

                elif clipitem_source.attrib['id'] == file_checking.attrib['id'] and filename is None:
                    clipitem.remove(clipitem_source)
                    clipitem.append(file_checking)

                elif filename is not None:
                    isUnique = True # this means the file is NOT in the list and needs to be added

        if isUnique == True: # adds file to list
            unique_files.append(clipitem_source)
            isUnique = False

        enabled = clipitem.find('enabled')
        if (enabled.text == 'TRUE'):
            track.remove(clipitem)

# remember to add the AUDIO part back in

print ("writing output...")
tree.write('sample_xmls_output/OUTPUT.xml')