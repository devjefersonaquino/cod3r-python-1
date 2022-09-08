a = ' valor' #True
a = 0 #False
a = -0000000.1 #True
a = '' #False
a = '     ' #True
a = [] #False
a = () #False
a = {} #False

if a:
    print('Existe!!!')
else:
    print('Não existe ou é zero ou é vazio...')