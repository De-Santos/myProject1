products = {
    "cucumber": ["5", "10", "15", "8"],
    "apple": ["6"],
    "chery": ["9"],
    "rod": ["10", "100", "21", "43"],
}


def write_text_to_file(lit):
    f = open("tags.txt", "a")
    f.write(lit + "\n")
    f.close()


def baz(rast):
    for i in rast:
        write_text_to_file(lit=i)


while len(products):
    a = input("введите продукт: ")
    if a in products.keys():
        baz(rast=products[a])
        products.pop(a)
    else:
        print("ERROR")

print("пусто")
