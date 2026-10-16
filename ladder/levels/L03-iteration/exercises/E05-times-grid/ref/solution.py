def times_grid():
    n=int(input("N: ")); total=0
    for row in range(1,n+1):
        values=[]
        for col in range(1,n+1): values.append(str(row*col)); total+=row*col
        print(" ".join(values))
    print(f"Total: {total}")
if __name__=="__main__": times_grid()
