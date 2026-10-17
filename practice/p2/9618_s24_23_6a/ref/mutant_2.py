# 9618_s24_23:6(a) MP5: string-concat
# Provided display interface: this Python adapter records the filename by printing it.
def Display(Filename):
    print(Filename)

def Progress(Percent,Root):
    StepValue=Percent//10+1
    Filename=Root+'-'+str(StepValue)+'.png'
    Display(Filename)
