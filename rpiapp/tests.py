from django.test import TestCase

# Create your tests here.

# s = tuple(map(lambda *x: x, (tuple([i for i in range(2018, 2050)]))))
#
# for i in s:
#     print(tuple(str(str(str(int(i[0])) + '-' + str(int(i[0] + 1))) + ', ' + str(str(int(i[0])) + '-' + str(int(i[0] + 1)))).split(',')))
#


# x = ['Test subject', 'Test subject 2', 'Bangla', 'English']
#
# y = map(lambda *p: p, x)
# for i in y:
#
#     print(next(y))


x = [('Test subject',), ('Test subject 2',), ('Bangla',), ('English',)]
s = [('Test subject',), ('Test subject 2',), ('Bangla',), ('English',)]

y = [x[i] for i in range(0,4)]


def oo():
    for i in range(0,4):
        valu = x[i]
        print(valu)


print(oo())
