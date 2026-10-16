PREDICTED: list[str] = ["3","2","3.4","3 7","ID-42","34","Mean is 3.4!"]
PREFIX="ID-"
def run_trace():
    total,count=17,5; mean=total/count
    print(total//count); print(total%count); print(mean)
    count+=2; total=total-count*2; print(f"{total} {count}")
    print(PREFIX+"42"); print(int(mean*10)); print(f"Mean is {mean}!")
if __name__=="__main__": run_trace()
