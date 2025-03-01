def copy_file(source, copy):
    with open(source, "r") as src:
        content = src.read()
    with open(copy, "w") as cp:
        cp.write(content)


copy_file("A.txt", "B.txt")
