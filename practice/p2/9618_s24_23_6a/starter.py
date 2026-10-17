# Provided display interface: this Python adapter records the filename by printing it.
def Display(Filename):
    print(Filename)

def Progress(Percent,Root):
    raise NotImplementedError
