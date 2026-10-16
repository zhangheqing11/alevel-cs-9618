ProductName = [""] * 10      # STRING, 10 elements
ProductPrice = [0.0] * 10    # REAL, 10 elements
NumberProducts = 0           # INTEGER


def ReadProducts(FileName: str) -> None:
    global NumberProducts
    try:
        with open(FileName, encoding="utf-8") as Source:
            for Line in Source:
                Name, Price = Line.rstrip("\n").split(",")
                ProductName[NumberProducts] = Name
                ProductPrice[NumberProducts] = float(Price)
                NumberProducts = NumberProducts + 1
    except FileNotFoundError:
        print("File not found")


def main() -> None:
    ReadProducts("Products.txt")
    if NumberProducts == 0:
        print("No products")
    else:
        Total = 0.0
        for Index in range(NumberProducts):
            print(f"{ProductName[Index]}: {ProductPrice[Index]:.2f}")
            Total = Total + ProductPrice[Index]
        print(f"Total: {Total:.2f}")


if __name__ == "__main__":
    main()
