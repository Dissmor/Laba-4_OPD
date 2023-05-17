import os

def Search(fileName):
    i = 0
    iMax = 0
    strRes = 'ьыъ'
    strWords = ''
    f = open(fileName, 'r')
    for line in f:
        strWords = strWords + ' ' + line.replace('\n', '')
    f.close()
    os.remove(fileName)
    arrWords = strWords.split(' ')
    for strWord in arrWords:
        if (arrWords.count(strWord) >= iMax):
            iMax = arrWords.count(strWord)
    for strWord in arrWords:
        if (arrWords.count(strWord) == iMax):
            if (strRes > strWord or strRes == 'ьыъ'):
                strRes = strWord
    return  strRes