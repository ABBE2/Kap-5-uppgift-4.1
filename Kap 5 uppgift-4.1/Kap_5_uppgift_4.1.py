a = int(input("a="))
b = int(input("b="))
c = int(input("c="))

if a < b and b < c:
    print('')
elif a < b:
    print('antingen ar a mindre an b eller b mindre an c')
elif b < c:
    print('antingen ar a mindre an b eller b mindre an c')
else:
    print('')