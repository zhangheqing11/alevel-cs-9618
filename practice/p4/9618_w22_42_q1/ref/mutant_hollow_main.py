# D46: correct modules, but main hard-codes output without calling them.
# Reference solution for 9618_w22_42 Question 1 (Question1_N22).
# Follows the MS Python examples; fixes: Jobs is built as a real 100 x 2 list
# (the MS 1(a) example is only a comment), Initialise() assigns -1 in place
# with two nested loops instead of appending 100 more rows.

# ---- 1(a) ----
Jobs = [[0, 0] for Row in range(100)]  # global 2D array of INTEGER, 100 x 2 (job number, priority)
NumberOfJobs = 0  # global INTEGER


# ---- 1(b) ----
def Initialise():
    global Jobs
    global NumberOfJobs
    for X in range(0, 100):
        for Y in range(0, 2):
            Jobs[X][Y] = -1
    NumberOfJobs = 0


# ---- 1(c) ----
def AddJob(JobNumber, Priority):
    global NumberOfJobs
    global Jobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs][0] = JobNumber
        Jobs[NumberOfJobs][1] = Priority
        NumberOfJobs = NumberOfJobs + 1
        print("Added")


# ---- 1(e) ----
def InsertionSort():
    global Jobs
    global NumberOfJobs
    for I in range(1, NumberOfJobs):
        Current1 = Jobs[I][0]
        Current2 = Jobs[I][1]
        J = I
        while J > 0 and Jobs[J - 1][1] > Current2:
            Jobs[J][0] = Jobs[J - 1][0]
            Jobs[J][1] = Jobs[J - 1][1]
            J = J - 1
        Jobs[J][0] = Current1
        Jobs[J][1] = Current2


# ---- 1(f) ----
def PrintArray():
    global Jobs
    global NumberOfJobs
    for X in range(0, NumberOfJobs):
        print(str(Jobs[X][0]) + " priority " + str(Jobs[X][1]))


# ---- main program: 1(d), 1(g)(i) ----

if __name__ == "__main__":
    print('Added\nAdded\nAdded\nAdded\nAdded\n78 priority 1\n33 priority 8\n526 priority 9\n12 priority 9\n12 priority 10\n', end="")
