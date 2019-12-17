import random
import math
import numpy as np
np.set_printoptions(threshold=np.inf)


# no_stu = int(input("Enter no of students: "))
# no_stu_cl = int(input("Enter no of students in one class: "))
# ext_ratio = int(input("Ratio for extra invidulators 1:"))

# no_blocks = math.ceil(no_stu/no_stu_cl)
# no_reliever = math.ceil(no_blocks/5)
# no_extras = math.ceil(no_blocks/ext_ratio)

# no_inv = no_blocks + no_reliever + no_extras
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

invd = [34, 39, 13, 38, 8, 30, 31, 17, 37, 32, 26,
        25, 29, 23, 34, 22, 32, 25, 17, 14]

# for x in range(50):
#     invd.append(random.randint(7, 40))


fitr = invd[:5]
comp = invd[:5]
# print(fitr)


arr = np.zeros((20, 180), dtype=np.int64)


# print(invd)
sor = [5]
incr = 0
while len(sor) != 0:
    i = j = 0
    sor = sorted(fitr)
    for z in range(len(sor)):
        if sor[z] == 0:
            j += 1
    if j != 0:
        for l in range(j):
            sor.remove(0)
    if len(sor) == 0:
        break
    for x in range(len(fitr)):

        for y in range(sor[0]):

            if fitr[x] != 0:
                arr[x][incr + y] = 1

        if fitr[x] != 0:
            fitr[x] -= sor[0]
    for g in range(len(comp)):
        if comp[g] == 0:
            i += 1
    if i != 0:
        for k in range(i):
            comp.remove(0)
    for g in range(len(comp)):
        comp[g] -= sor[0]
    for v in range(len(comp)):
        if comp[v] == 0:
            if len(fitr) != 20:
                le = invd[len(fitr)]
                fitr.append(le)

    incr += sor[0]
    comp = []
    comp.extend(fitr)


arr1 = arr.transpose()
# print(arr1)
for _ in range(180):
    print(_ + 1, arr1[_])
# print(arr1)

# runner = []
# random_list = []
# big = []

# for _ in range(5):
#     bran_len = len(depart[_])
#     runner.append(list(depart[_]))
#     bran_inv = math.ceil((no_inv * bran_len)/100)
#     random_list = []
#     for x in range(bran_inv):
#         rand = random.choice(runner[_])
#         random_list.append(rand)
#         runner[_].remove(rand)

#     big.append(random_list)

# for _ in range(5):
#     print(*big[_], sep='  {} \n'.format(name[_]))
