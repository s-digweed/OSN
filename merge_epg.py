import xml.etree.ElementTree as ET
import os, shutil, sys

lang = sys.argv[1]

android = f'epg-src/OSN_ANDROID_{lang}.xml'
legacy = f'epg-src/OSN_LEGACY_{lang}.xml'
output = f'epg-src/OSN_{lang}.xml'

if os.path.exists(android) and os.path.exists(legacy):
    base = ET.parse(android).getroot()
    extra = ET.parse(legacy).getroot()
    for elem in extra:
        base.append(elem)
    ET.ElementTree(base).write(output, encoding='UTF-8', xml_declaration=True)
    print(f'Merged {lang} files')
elif os.path.exists(android):
    shutil.copy(android, output)
    print(f'Only Android {lang} available')
elif os.path.exists(legacy):
    shutil.copy(legacy, output)
    print(f'Only Legacy {lang} available')
else:
    print(f'No {lang} files to merge')
