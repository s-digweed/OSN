import xml.etree.ElementTree as ET
import os

target_ids = {'5674','5673','4514','4513','5675','5676','311','312','216','224','209','220','223','211','203','202','217'}

if not os.path.exists('epg-src/OSN_LEGACY_EN_FULL.xml'):
    print('No Legacy EN file to filter')
    exit()

tree = ET.parse('epg-src/OSN_LEGACY_EN_FULL.xml')
root = tree.getroot()
new_root = ET.Element('tv')

for child in root:
    if child.tag == 'channel' and child.get('id') in target_ids:
        new_root.append(child)
    elif child.tag == 'programme' and child.get('channel') in target_ids:
        new_root.append(child)

ET.ElementTree(new_root).write('epg-src/OSN_LEGACY_EN.xml', encoding='UTF-8', xml_declaration=True)
print('Filtered EN done')

for tid in target_ids:
    count = sum(1 for c in new_root if c.tag == 'programme' and c.get('channel') == tid)
    name = next((c.find('display-name').text for c in new_root if c.tag == 'channel' and c.get('id') == tid), tid)
    print(f'{name} ({tid}): {count} programmes')
