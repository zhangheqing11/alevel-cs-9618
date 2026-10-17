# Provided display interface: this Python adapter records the filename by printing it.
def Display(Filename):
    print(Filename)

def Progress(Percent,Root):
    StepValue=Percent//10+1
    Filename=Root+'-'+str(StepValue)+'.bmp'
    Display(Filename)
