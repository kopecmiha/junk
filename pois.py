from PIL import Image
import os
import shutil
path = r'D:\загрузки\ваха цив 3\см\sm_units\\'
paps = os.listdir(path)
i = 0
for pap in paps:
    i+=1
    files = os.listdir(path + str(pap))
    papka = str(pap)
    anim = '#ANIMNAME_PRTO_' + papka + '\n' + papka
    print(anim)
    
    
##    pediaicons ICON
##    for file in files:
##        if file.lower().find('.pcx') > -1:
##            if file.find('32') == -1:
##                icon = icon + r'art\civilopedia\icons\units' + chr(92) + str(file) + '\n'
##    print(icon + str(i))
   
    '''
    циварты
    for file in files:
        if file.lower().find('.pcx') > -1:
            if file.find('32') == -1:
                shutil.copy(path + papka + '\\' + file, r'D:\загрузки\ваха цив 3\см\civart\\')
                print(file)
    '''
    '''
    иконки
    for file in files:
        if file.lower().find('.pcx') > -1:
            if file.find('32') > -1:
                shutil.copy(path + papka + '\\' + file, r'D:\загрузки\ваха цив 3\см\icons\\' + papka + '.pcx')
                print(file)
    '''
    
                      
                      

    
    
