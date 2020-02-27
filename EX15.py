def split_func(a):
    return a.split(" ")

def oppo(a):
    return a[::-1]


z = " ".join(oppo(split_func(input("Tell me a sentence : "))))

print("Result : " + z)