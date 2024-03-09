import itertools

if __name__ == "__main__":
    n = 3
    products = itertools.product("BRG", repeat=n)
    products = ["".join(prod) for prod in products]
    print(products)
    print(len(products))