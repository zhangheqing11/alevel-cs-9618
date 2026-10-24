# D46: correct modules, but main bypasses the required calls.
# StackVowel, StackConsonant: ARRAY[0:99] OF STRING.
StackVowel = [''] * 100
StackConsonant = [''] * 100
# VowelTop, ConsonantTop: INTEGER; next free index.
VowelTop = 0
ConsonantTop = 0


def PushData(Letter):
    global VowelTop, ConsonantTop
    if Letter == 'a' or Letter == 'e' or Letter == 'i' or Letter == 'o' or Letter == 'u':
        if VowelTop == 100:
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
    print('Vowel or Consonant: Vowel or Consonant: Vowel or Consonant: Vowel or Consonant: Vowel or Consonant: utxoe\n', end='')
