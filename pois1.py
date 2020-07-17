from PIL import Image
import os
paps = os.listdir('D:\Games\XCOM 2\XCom2-WarOfTheChosen\XComGame\Mods\\')
for pap in paps:
    files = os.listdir('D:\Games\XCOM 2\XCom2-WarOfTheChosen\XComGame\Mods\\' + str(pap))
    for file in files:
        if file.lower().find('xcommod') > -1:
            print('ActiveMods=' + file.replace('.XComMod', ''))
    
    
