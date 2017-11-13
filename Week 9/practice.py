length = int(input("Hy! How long you want your square to be?  "));
height = int(input("How tall you want your square to be?  "));

print(length, height);

def printer(length, height):
    for i in range(height):
        print("*" * length)

printer(length, height);