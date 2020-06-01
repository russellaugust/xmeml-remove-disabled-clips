import xml.etree.ElementTree as ET
from copy import deepcopy

tree = ET.parse('/Users/russellanderson/Desktop/XML Testing/REEL 1_25_TEST_NESTED AND ONE EXTRA.xml')
root = tree.getroot()

unique_files = [] # storage for the file element. this MAY need to exist outside this scope. not sure how this works across sequences yet. 

for track in root.findall('./sequence/media/video/track'):
    for clipitem in track.findall('clipitem'):

        isUnique = False
        file_current = clipitem.find('file') # get the unique file-id
        fileid_current = file_current.attrib['id'] # get the unique file-id
        filename = clipitem.find('file/name') # this is more important when i need check if the file content exists

        if len(unique_files) == 0: # needs to add an item first. happens once.
            unique_files.append(file_current)
        else:
            for file_checking in unique_files:
                if fileid_current == file_checking.attrib['id'] and filename is not None:
                    isUnique = False
  
                elif fileid_current == file_checking.attrib['id'] and filename is None:
                    clipitem.remove(file_current)
                    clipitem.append(file_checking)

                elif filename is not None:
                    isUnique = True # this means the file is NOT in the list and needs to be added

        if isUnique == True: # adds file to list
            unique_files.append(file_current)
            isUnique = False

        enabled = clipitem.find('enabled')
        if (enabled.text == 'TRUE'):
            track.remove(clipitem)

for track in root.findall('./sequence/media/audio/track'):
    print ('=============== TRACK ================')
    for clipitem in track.findall('clipitem'):
        print ('============== CLIP =================')

        isUnique = False

        file_current = clipitem.find('file') # get the unique file-d
        fileid_current = file_current.attrib['id'] # get the unique file-d
        
        filename = clipitem.find('file/name') # this is more important when i need check if the file content exists

        # is file present in files. Add the first, otherwise...
        if len(unique_files) == 0: # needs to add an item first
            unique_files.append(file_current)
        else:
            for file_checking in unique_files:
                if fileid_current == file_checking.attrib['id'] and filename is not None:
                    isUnique = False
                    
                elif fileid_current == file_checking.attrib['id'] and filename is None:
                    clipitem.remove(file_current)
                    clipitem.append(file_checking)

                elif filename is not None:
                    isUnique = True # this means the file is NOT in the list and needs to be added

        if isUnique == True: # adds file to list
            unique_files.append(file_current)
            isUnique = False

        enabled = clipitem.find('enabled')
        if (enabled.text == 'TRUE'):
            track.remove(clipitem)

tree.write('/Users/russellanderson/Desktop/XML Testing/OUTPUT.xml')