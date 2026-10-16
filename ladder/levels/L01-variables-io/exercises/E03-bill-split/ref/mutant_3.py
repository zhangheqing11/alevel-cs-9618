SERVICE_RATE=.1
def split_bill():
 b=int(input()); p=int(input()); t=b*1.1; print(f"Total: {t:.2f}"); print(f"Each: {t/p:.2f}")
