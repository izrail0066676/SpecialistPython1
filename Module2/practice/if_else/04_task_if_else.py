# Дано целое число.
# Если оно делится на 3 без остатка - вывести ”Foo”,
# если делится на 5 - вывести “Bar”,
# а если делится на 3 и на 5 - вывести “Foobar”.
# Для всех остальных случаев не выводить ничего.

# TODO: your code here
number = int(input())
n = 15
if 3 / n:
    print("foo")
if 5 / n:
    print("bar")
if 3 / n and 5 / n:
    print("Foobar")

