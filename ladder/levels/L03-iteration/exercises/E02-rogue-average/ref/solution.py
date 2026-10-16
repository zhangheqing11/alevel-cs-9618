def rogue_average():
    number=int(input("Number (-1 to stop): ")); count=total=0
    while number!=-1:
        count+=1; total+=number; number=int(input("Number (-1 to stop): "))
    if count==0: print("No data")
    else:
        print(f"Count: {count}"); print(f"Total: {total}"); print(f"Average: {total/count:.1f}")
if __name__=="__main__": rogue_average()
