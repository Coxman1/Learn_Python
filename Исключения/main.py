names = {
    'Arthur': 2,
}

try:
    print(names['AAA'])
except KeyError:
    pass

a=1
b=0
try:
    c=a/b
except ZeroDivisionError:
    pass