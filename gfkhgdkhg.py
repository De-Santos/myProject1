rost = {"q": ["10"], "w": ["11", "2", "3"], "ras": ["13", "101", "5", "6"]}


def write_text_to_file(lit):
    f = open("tags.txt", "a")
    f.write(lit + "\n")
    f.close()


for x in list(rost):
    print(x)
    write_text_to_file(lit=x)
