import xlsxwriter
import random
import math
import numpy as np
np.set_printoptions(threshold=np.inf)

invd = []
noOfExams = int(input("Enter no of exams: "))
for _ in range(noOfExams):

    no_stu = int(input("Enter no of students: "))
    no_stu_cl = int(input("Enter no of students in one class: "))
    ext_ratio = int(input("Ratio for extra invidulators 1:"))

    no_blocks = math.ceil(no_stu/no_stu_cl)
    no_reliever = math.ceil(no_blocks/5)
    no_extras = math.ceil(no_blocks/ext_ratio)

    no_inv = no_blocks + no_reliever + no_extras
    invd.append(no_inv)

# print(no_inv)


# no_inv = int(input("Enter the no of invidulations: "))

name = ['Mechanical', 'Civil', 'Aero', 'Electrical', 'Computer']


mechanical_Department = ("Kiran Joshi",
                         "Parth Chaudhari",
                         "Arti Joshi",
                         "Jayendra Tamboli",
                         "Rohit Mishra",
                         "Jitendra Joshi",
                         "Devi Patil",
                         "Chanda Jain",
                         "Sachin D'cruze",
                         "Lucky Rao",
                         "Tejal Narang",
                         "Bharat Patel",
                         "Vivek Misra",
                         "Rajesh Patel",
                         "Kamini Vemulakonda",
                         "Arati Nagarkar",
                         "Ankit D'cruz",
                         "Harinder Kaur",
                         "Nila Chaudhari",
                         "Devadas Narang", )

civil_Department = ("Kiran Joshi",
                    "Parth Chaudhari",
                    "Arti Joshi",
                    "Jayendra Tamboli",
                    "Rohit Mishra",
                    "Jitendra Joshi",
                    "Devi Patil",
                    "Chanda Jain",
                    "Sachin D'cruze",
                    "Lucky Rao",
                    )

aero_Department = ("Arati Nagarkar",
                   "Ankit D'cruz",
                   "Harinder Kaur",
                   "Nila Chaudhari",
                   "Devadas Narang", )

electrical_Department = ("Kiran Joshi",
                         "Parth Chaudhari",
                         "Arti Joshi",
                         "Jayendra Tamboli",
                         "Rohit Mishra",
                         "Jitendra Joshi",
                         "Devi Patil",
                         "Chanda Jain",
                         "Sachin D'cruze",
                         "Lucky Rao",
                         "Tejal Narang",
                         "Bharat Patel",
                         "Vivek Misra",
                         "Rajesh Patel",
                         "Kamini Vemulakonda",
                         "Arati Nagarkar",
                         "Ankit D'cruz",
                         "Harinder Kaur",
                         "Nila Chaudhari",
                         "Devadas Narang",
                         "Reena Kulkarni",
                         "Jagdish Patil",
                         "Gayatri Misra",
                         "Aniket Patel",
                         "Devika Tamboli",
                         "Raja Patel",
                         "Kshitija Misra",
                         "Urvi Jain",
                         "Shantanu Bachchan",
                         "Madhuri Gadhavi",)

computer_Department = ("Kiran Joshi",
                       "Jyotsna Narang",
                       "Krishna Patil",
                       "Karthik Nibhanupudi",
                       "Vikram Nagarkar",
                       "Ashwin Jain",
                       "Parth Chaudhari",
                       "Arti Joshi",
                       "Jayendra Tamboli",
                       "Rohit Mishra",
                       "Jitendra Joshi",
                       "Devi Patil",
                       "Chanda Jain",
                       "Sachin D'cruze",
                       "Lucky Rao",
                       "Tejal Narang",
                       "Bharat Patel",
                       "Vivek Misra",
                       "Rajesh Patel",
                       "Kamini Vemulakonda",
                       "Arati Nagarkar",
                       "Ankit D'cruz",
                       "Harinder Kaur",
                       "Nila Chaudhari",
                       "Devadas Narang",
                       "Reena Kulkarni",
                       "Jagdish Patil",
                       "Gayatri Misra",
                       "Aniket Patel",
                       "Devika Tamboli",
                       "Raja Patel",
                       "Kshitija Misra",
                       "Urvi Jain",
                       "Shantanu Bachchan",
                       "Madhuri Gadhavi",)

depart = [mechanical_Department, civil_Department,
          aero_Department, electrical_Department, computer_Department]

comb = []

for _ in range(len(depart)):
    for x in range(len(depart[_])):
        comb.append(depart[_][x])

# print(*comb, sep=("\n"))

new_list = []
for index, val in enumerate(comb):
    new_list.append(val)
    new_list.append(index + 1)


comb_dict = {new_list[i]: new_list[i + 1] for i in range(0, len(new_list), 2)}
### invd is total invidulations ###
# invd = [34, 39, 13, 38, 8, 30, 31, 17, 37, 32, 26,
#         25, 29, 23, 34, 22, 32, 25, 17, 14]


days = noOfExams
# days = 20
teachers = 180

### creating empty matrix ###
arr = np.zeros((days, teachers), dtype=np.int64)


indexCustomTeacher = []  # teachers who want specified days
customTeacherDays = []  # above teachers specified days

dayz = 0
custom = input(
    "If any teachers require custom invidulations press y/Y : ").lower()
if custom == 'y':
    dayz = int(input("How many teachers: "))
    for _ in range(dayz):
        work_days, * \
            teacherName = input(
                f"Enter {_ + 1} teacher's working days and their name: ").split()
        indexCustomTeacher.append(
            comb_dict[f"{teacherName[0]} {teacherName[1]}".title()])
        customTeacherDays.append(int(work_days))

if dayz:
    noCustomTeachers = dayz
else:
    noCustomTeachers = 0
### individual branch percentage ###
arr1 = arr.transpose()
branch_per = []
for _ in range(len(depart)):
    branch_per.append(((len(comb) * len(depart[_]))/100))

# print(branch_per)
branch_r = []
branch_x = []
branch_req = []
branch_zero = []

### everydays separate no of invidulators required ###
for x in range(len(invd)):
    for _ in range(len(branch_per)):
        varr = (math.ceil((branch_per[_] * invd[x])/100))
        branch_r.append(varr)
        branch_x.append(len(depart[_]) - varr)
    branch_req.append(branch_r)
    branch_zero.append(branch_x)
    branch_r = []
    branch_x = []
print(branch_req)

### algorithm to fill matrix with invidulator assignment ###
testr = tests = 0
x = 0
for _ in range(days):
    x = 0
    lenty = 0
    for y in range(5):  # no of branches
        tests = 0
        while True:
            tests = 0
            for test1 in range(days):
                tests += arr1[x][test1]
            if tests == 5:
                x += 1
            elif tests != 5:
                break
        for z in range(branch_req[_][y]):
            if x == len(depart[y]):
                break
            testr = 0
            for test in range(days):
                testr += arr1[x][test]
            if testr != 5:
                arr1[x][_] = 1
            x += 1
        lenty += len(depart[y])
        change = lenty - x
        x += change

### algorithm to assign specific days for requested teachers ###
for x in range(noCustomTeachers):
    dd = 0
    for _ in range(days):
        if dd != customTeacherDays[x]:
            dd += arr1[indexCustomTeacher[x]-1][_]
        else:
            arr1[indexCustomTeacher[x]-1][_] = 0


### algorithm for summation of individual day ###
summ = 0
sub = []
for _ in range(days):
    for x in range(teachers):
        summ += arr[_][x]
    sub.append(summ)
    summ = 0

### algorithm for substracted list ###
sub2 = []
hh = 0
for _ in range(days):
    hh = (sub[_])
    sub2.append(hh)

neww = [x1 - x2 for (x1, x2) in zip(invd, sub2)]


### algorithm for extra teachers assignment ###
flag = 1
tests = 0
x = len(comb)
while flag != 0:
    for _ in range(days):
        testr = 0
        tests = 0
        for test in range(days):
            testr += arr1[x][test]
            if neww[test] > 0:
                tests += 1
        if tests == 0:
            flag = 0
        if testr != 5:
            if arr1[x][_] != 1:
                if neww[_] > 0:
                    arr1[x][_] = 1
                    neww[_] -= 1
        else:
            break

    x += 1


for _ in range(teachers):
    print(_ + 1, arr1[_])


arr2 = list(arr1.transpose())

### algorithm for conversion of numpyarray(matrix) to 2D-list ###
arr3 = []
arr4 = []
for _ in range(days):
    for x in range(teachers):
        arr3.append(arr2[_][x])
    arr4.append(arr3)
    arr3 = []
arr5 = []

### writing matrix to the excel file ###
workbook = xlsxwriter.Workbook('Simran.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True, 'font_size': 12})
worksheet.set_column(0, 0, 30)


for _ in range(80):
    comb.append("extra")

worksheet.set_header('Hello')
worksheet.set_header('&L&G', {'image_left': 'logo.jpg'})

cell_format1 = workbook.add_format(
    {'bold': True, 'font_name': 'Lucida Sans Typewriter', 'font_size': 15})
cell_format = workbook.add_format(
)
cell_format.set_pattern(1)  # This is optional when using a solid fill.
cell_format.set_bg_color('white')
# cell_format.set_fg_color("green")
cell_format.set_border(1)

row = 2
for col, data in enumerate(invd):
    worksheet.write(row, col+1, data, bold)
col = 0

for row, data in enumerate(comb):
    worksheet.write(row + 4, col, data, cell_format1)
row = 4
for col, data in enumerate(arr4):
    for _ in range(teachers):
        if data[_] == 0:
            # converting individual integer lists to string lists and making 0 = '' ###
            data[_] = str(data[_])
            data[_] = ''
    worksheet.write_column(row, col+1, data, cell_format)

workbook.close()
