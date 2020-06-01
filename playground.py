import xml.etree.ElementTree as ET
from copy import deepcopy

tree = ET.parse('/Users/russellanderson/Desktop/XML Testing/REEL 1_25_TEST_NESTED AND ONE EXTRA.xml')
root = tree.getroot()

for track in root.findall('./sequence/media/video/track'):
    for clipitem in track.findall('clipitem'):
        if clipitem.find('sequence') is not None:
            print (clipitem.find('sequence').attrib['id'])

        #fileid_current = file_current.attrib['id'] # get the unique file-id
        
        #filename = clipitem.find('file/name') # this is more important when i need check if the file content exists
