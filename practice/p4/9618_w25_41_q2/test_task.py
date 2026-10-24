"""9618_w25_41 Q2 exact MS: capacity, containment, empty return and formatted trains."""
import runpy
from testkit import run_script,output_lines


def test_2ai_aii_train(sol):
    """9618_w25_41:2(a)(i) MP2-MP4; 2(a)(ii) MP2-MP3."""
    t=sol.Train('X11',28)
    assert (t._Train__TrainIDNumber,t._Train__Route)==('X11',28)
    assert (t.GetTrainIDNumber(),t.GetRoute())==('X11',28)


def test_2ci_station_initial_state(sol):
    """9618_w25_41:2(c)(i) MP1-MP3: private state, ten slots, zero trains."""
    s=sol.Station('ABC',3)
    assert (s._Station__StationID,s._Station__NumberPlatforms,s._Station__NumberTrains)==('ABC',3,0)
    assert isinstance(s._Station__Trains,list) and len(s._Station__Trains)==10


def test_2cii_capacity_and_storage(sol):
    """9618_w25_41:2(c)(ii) MP2-MP4: add to capacity then reject without state change."""
    s=sol.Station('T',2);a=sol.Train('A',1);b=sol.Train('B',2);c=sol.Train('C',3)
    assert s.AddTrain(a) is True
    assert s._Station__NumberTrains==1 and s._Station__Trains[0] is a
    assert s.AddTrain(b) is True
    assert s._Station__NumberTrains==2 and s._Station__Trains[1] is b
    before=list(s._Station__Trains)
    assert s.AddTrain(c) is False
    assert s._Station__Trains==before and s._Station__NumberTrains==2


def test_2ciii_empty_string(sol):
    """9618_w25_41:2(c)(iii) MP1-MP2: empty station returns exact QP string."""
    assert sol.Station('NT1',2).GetTrains()=='There are no trains'


def test_2ciii_getters_formatted_return(sol):
    """9618_w25_41:2(c)(iii) MP1,MP3-MP6: getter protocol and QP example format."""
    class T:
        def __init__(self,n,r):self.n=n;self.r=r
        def GetTrainIDNumber(self):return self.n
        def GetRoute(self):return self.r
    s=sol.Station('NT1',2);s.AddTrain(T('48RTG',43));s.AddTrain(T('6UFH',12))
    assert output_lines(s.GetTrains())==['The trains at station NT1 are:','48RTG on route number 43','6UFH on route number 12']


def test_2b_di_main_instances(candidate_path):
    """9618_w25_41:2(b) MP1-MP2; 2(d)(i) MP1-MP2."""
    ns=runpy.run_path(str(candidate_path),run_name='__main__')
    values=[]
    for value in ns.values():
        values.extend(value if isinstance(value,list) else [value])
    trains=[t for t in values if isinstance(t,ns['Train'])]
    assert {(t.GetTrainIDNumber(),t.GetRoute()) for t in trains}=={('12ADV',134),('33ART',20),('9FKF',3),('21VBC',24)}
    stations=[s for s in values if isinstance(s,ns['Station'])]
    assert {(s._Station__StationID,s._Station__NumberPlatforms) for s in stations}=={('STH',2),('NTH',1)}


def test_2diii_screenshot(candidate_path):
    """9618_w25_41:2(d)(ii) MP1-MP4; 2(d)(iii) MP1-MP2: full once, two formatted stations."""
    r=run_script(candidate_path);assert r.returncode==0,r.stderr
    assert r.lines==['Station is full','The trains at station STH are:',
                     '12ADV on route number 134','33ART on route number 20',
                     'The trains at station NTH are:','21VBC on route number 24']
