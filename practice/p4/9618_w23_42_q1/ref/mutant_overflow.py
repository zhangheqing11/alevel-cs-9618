# 9618_w23_42:1(b)(i) MP3; stack-array: accepts 101st vowel.
# StackVowel, StackConsonant: ARRAY[0:99] OF STRING.
StackVowel = [''] * 100
StackConsonant = [''] * 100
# VowelTop, ConsonantTop: INTEGER; next free index.
VowelTop = 0
ConsonantTop = 0


def PushData(Letter):
    global VowelTop, ConsonantTop
    if Letter == 'a' or Letter == 'e' or Letter == 'i' or Letter == 'o' or Letter == 'u':
        if VowelTop > 100:
            print('Vowel stack full')
        else:
            StackVowel[VowelTop] = Letter
            VowelTop += 1
    else:
        if ConsonantTop == 100:
            print('Consonant stack full')
        else:
            StackConsonant[ConsonantTop] = Letter
            ConsonantTop += 1


def ReadData():
    try:
        with open('StackData.txt') as DataFile:
            for Line in DataFile:
                PushData(Line.rstrip('\r\n'))
    except OSError:
        print('File not found')


def PopVowel():
    global VowelTop
    if VowelTop == 0:
        return 'No data'
    VowelTop -= 1
    return StackVowel[VowelTop]


def PopConsonant():
    global ConsonantTop
    if ConsonantTop == 0:
        return 'No data'
    ConsonantTop -= 1
    return StackConsonant[ConsonantTop]


if __name__ == '__main__':
    ReadData()
    Letters = ''
    for X in range(5):
        Flag = False
        while not Flag:
            Choice = input('Vowel or Consonant: ').lower()
            if Choice == 'vowel':
                DataAccessed = PopVowel()
            elif Choice == 'consonant':
                DataAccessed = PopConsonant()
            else:
                continue
            if DataAccessed == 'No data':
                print('No letters left in that stack')
            else:
                Letters += DataAccessed
                Flag = True
    print(Letters)
