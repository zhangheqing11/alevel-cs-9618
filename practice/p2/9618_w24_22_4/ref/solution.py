import time
Tick = 0  # Given global INTEGER, milliseconds, updated by the environment.
_ClockOrigin = time.monotonic_ns()
# Provided Python adapter for reading the externally advancing Tick.
# The learner reads this function; the pseudocode reads Tick directly.
def ReadTick():
    global Tick
    Tick = (time.monotonic_ns()-_ClockOrigin)//1000000
    return Tick

def Timer(Mins,Secs):
    EndTick=ReadTick()+1000*(Mins*60+Secs)
    WarningTick=EndTick-30000
    while ReadTick()<WarningTick:
        pass
    print('30 seconds to go')
    while ReadTick()<EndTick:
        pass
    print('The time is up!')
