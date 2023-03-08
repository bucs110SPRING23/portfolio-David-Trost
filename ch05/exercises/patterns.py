def star_pyramid(rows):
    for i in range(1, rows+1):
        print("*" * i)

def rstar_pyramid(rows):
    for i in range(rows,0,-1):
        print("*" * i)

levels=int(input("Enter the desired pyramid height:"))

star_pyramid(levels)
rstar_pyramid(levels)

