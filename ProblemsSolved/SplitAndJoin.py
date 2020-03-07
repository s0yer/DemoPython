# Split and Join

line = "To become the best you need to improve"

def split_and_join(line):
    s = line.split(" ")
    v = "-".join(s)

    v = line.split("-")
    k = "*".join(v)

    print(v)
    print(k)

    return v

result = split_and_join(line)
print(result)