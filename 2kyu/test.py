import itertools

if __name__ == "__main__":
    n = 3
    products = itertools.product("BRGye", repeat=n)
    products = ["".join(prod) for prod in products]
    print(products)
    print(len(products))