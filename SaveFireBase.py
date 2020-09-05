from xml.etree.ElementTree import parse
import urllib.request as ur

tree = parse('./data/test.xml')
root = tree.getroot()

row = root.findall("row")
total_recipe_count = len(row)

#메뉴 이름
menuname = [x.findtext("RCP_NM") for x in row]
#재료 이름
material = [x.findtext("RCP_PARTS_DTLS") for x in row]
menual = []

#레시피 
for r in range(1, total_recipe_count+1):
    menual.append([])
    for n in range(1, 21):
        # print('row[r] : ', row[r-1])
        # print('row[r].findtext : ', row[r-1].findtext("MANUAL" +  str(n).zfill(2)))
        temp = row[r-1].findtext("MANUAL" +  str(n).zfill(2))
        if temp != "":
            menual[r-1].append(temp)
        else:
            break 

#이미지 링크 저장
img = [x.findtext("ATT_FILE_NO_MAIN") for x in row]

#이미지 다운로드
# for i, m in zip(range(0, total_recipe_count), menuname):
#     ur.urlretrieve(img[i], './img/' + m + '.png')

#테스트
# for x in range(0, total_recipe_count+1):
#     result = ''
#     try:
#         result = material[x].index('달걀')
#     except:
#        continue
        
#     print(menuname[x])
    

# print('row', row)
# print('menuname', menuname)
# print('material', material)
# print(menual)