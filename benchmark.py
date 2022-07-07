"""Benchmark experiments to compare performance of different methods."""

import timeit


def main():
    test_value = [x for x in range(500000)]
    print("TESTING WITH: ", test_value)
    compare_iterate_data(test_value)


def compare_add_data(test_value: list):
    print("List: ", timeit.timeit(
        stmt=f"""\
mylist = []
for i in {test_value}:
    mylist.append(i)
"""))

    print("Dict: ", timeit.timeit(
        stmt=f"""\
test_list = {test_value}
mydict = dict()
for i in range(len(test_list)):
    mydict[i] = test_list[i]
"""))

    print("Set: ", timeit.timeit(
        stmt=f"""\
mySet = set()
for i in {test_value}:
    mySet.add(i)
"""))


def compare_iterate_data(test_value: list):
    print("List: ", timeit.timeit(
        stmt=f"""\
for i in mylist:
    unused = i           
""",
        setup=f"""\
mylist = []
for i in {test_value}:
    mylist.append(i)
"""))

    print("Dict: ", timeit.timeit(
        stmt=f"""\
for i in mydict:
    unused = mydict[i]
""",
        setup=f"""\
test_list = {test_value}
mydict = dict()
for i in range(len(test_list)):
    mydict[i] = test_list[i]
"""))

    print("Set: ", timeit.timeit(
        stmt=f"""\
for i in mySet:
    unused = i
""",
        setup=f"""\
mySet = set()
for i in {test_value}:
    mySet.add(i)
"""))


def compare_unique_id_genration():
    print("random.randint() ", timeit.timeit(
        stmt="random.randint(0, 32)", setup="import random"))
    print("uuld.uuld4() ", timeit.timeit(
        stmt="uuld.uuld4() ", setup="import uuld"))
    print("uuld.uuld1() ", timeit.timeit(
        stmt="uuld.uuld1()", setup="import uuld"))
    print("hashlib.md5() ", timeit.timeit(
        stmt="hashlib.md5()", setup="import hashlib"))
    print("hashlib.sha256() ", timeit.timeit(
        stmt="hashlib.sha256()", setup="import hashlib"))
    print("time.time() ", timeit.timeit(
        stmt="time.time()", setup="import time"))


if __name__ == "__main__":
    main()
