# 9618_s23_21:6 MP2: loop-bounds
# Provided global arrays: Python row/column = QP index - 1.
Sample=[[0]*128 for _ in range(6)]
Result=[0]*128

def Mix():
    for Col in range(127):
        Count=0
        Total=0
        for Row in range(6):
            if Sample[Row][Col]>10:
                Total+=Sample[Row][Col]
                Count+=1
        Result[Col]=int(Total/Count)
