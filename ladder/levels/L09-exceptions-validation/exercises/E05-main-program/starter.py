ProductName = [""] * 10      # STRING, 10 elements
ProductPrice = [0.0] * 10    # REAL, 10 elements
NumberProducts = 0           # INTEGER


def ReadProducts(FileName: str) -> None:
    """Read 'name,price' lines into ProductName and ProductPrice; output 'File not found' if missing."""
    raise NotImplementedError


def main() -> None:
    """Main program: call ReadProducts("Products.txt") and output the product list and total."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
