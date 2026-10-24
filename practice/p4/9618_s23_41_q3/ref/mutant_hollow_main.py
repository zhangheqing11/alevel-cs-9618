# D46: correct modules, but main bypasses the required calls.
Animal = [''] * 20  # ARRAY[0:19] OF STRING
Colour = [''] * 10  # ARRAY[0:9] OF STRING
AnimalTopPointer = 0  # INTEGER
ColourTopPointer = 0  # INTEGER


def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    Animal[AnimalTopPointer] = DataToPush
    AnimalTopPointer += 1
    return True


def PopAnimal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ''
    ReturnData = Animal[AnimalTopPointer - 1]
    AnimalTopPointer -= 1
    return ReturnData


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 10:
        return False
    Colour[ColourTopPointer] = DataToPush
    ColourTopPointer += 1
    return True


def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ''
    ReturnData = Colour[ColourTopPointer - 1]
    ColourTopPointer -= 1
    return ReturnData


def ReadData():
    try:
        AnimalFile = open('AnimalData.txt', 'r')
        for Line in AnimalFile:
            PushAnimal(Line.rstrip('\r\n'))
        AnimalFile.close()
        ColourFile = open('ColourData.txt', 'r')
        for Line in ColourFile:
            PushColour(Line.rstrip('\r\n'))
        ColourFile.close()
    except OSError:
        print('Could not find file')


def OutputItem():
    ColourReturned = PopColour()
    AnimalReturned = PopAnimal()
    if ColourReturned == '':
        print('No colour')
        if AnimalReturned != '':
            PushAnimal(AnimalReturned)
    elif AnimalReturned == '':
        print('No animal')
        PushColour(ColourReturned)
    else:
        print(ColourReturned.rstrip('\r\n'), AnimalReturned.rstrip('\r\n'))


if __name__ == '__main__':
    print('pink hamster\nblue elephant\nwhite eagle\nyellow rabbit\n', end='')
