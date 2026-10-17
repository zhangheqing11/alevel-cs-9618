# 9618_s24_23:6(a) MP3: div-mod
# Provided display interface: this Python adapter records the filename by printing it.
def Display(Filename):
    print(Filename)

def Progress(Percent,Root):
    StepValue=Percent//10
    Filename=Root+'-'+str(StepValue)+'.bmp'
    Display(Filename)
