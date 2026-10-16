def mark_summary():
    m1=int(input("Mark 1: ")); m2=int(input("Mark 2: ")); m3=int(input("Mark 3: ")); total=m1+m2+m3; average=total/3
    print(f"Total: {total}"); print(f"Average: {average:.1f}")
if __name__=="__main__": mark_summary()
