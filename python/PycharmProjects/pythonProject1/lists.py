from student import Student
student1 = Student("William", "History", 3.4, True)
student1.print()

# lists[]
friends = ["Dale", "Joe", "Ed", 2, True, "Ellen"]

# 2d list
num_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in num_grid:
    for col in row:
        print(col)
    print("row done")
print("grid done")


# function they must be defined before used in script
def my_func(name: str):
    print("hello " + name)
    if True:
        return 1
    # elif False:
    #     return 2
    # else:
    #     return 3


# COOL if in usage with try

try:
    if "a" in "abc":
        print("if in")
except ZeroDivisionError as err:
    print(err)
finally:
    print("finally")


print(my_func(friends[0]))

# print(friends)
# print(friends[1])
# print(friends[1:])   # print from to end
# print(friends[1:4])  # print element 1 to 3
# print(friends[-1])   # print last element
# print(friends[9:2])  # print element 1 to 3

# tuples ()  - immutable list
coordinate = (2, 3)
print(coordinate)

# dictionary {}

months = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March"
}
print(months["Jan"])

i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1):
    print(i)

# files
try:
    file_stream = open("app.py", "r")
    if file_stream.readable():
        print(file_stream.read())

    file_stream.close()
except ZeroDivisionError:
    print("a")
