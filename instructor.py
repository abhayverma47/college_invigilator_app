import math
import random


no_stu = int(input("Enter no of students: "))
no_stu_cl = int(input("Enter no of students in one class: "))
ext_ratio = int(input("Ratio for extra invidulators 1:"))

no_blocks = math.ceil(no_stu/no_stu_cl)
no_reliever = math.ceil(no_blocks/5)
no_extras = math.ceil(no_blocks/ext_ratio)

no_inv = no_blocks + no_reliever + no_extras
print(no_inv)


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


runner = []
random_list = []
big = []

for _ in range(5):
    bran_len = len(depart[_])
    runner.append(list(depart[_]))
    bran_inv = math.ceil((no_inv * bran_len)/100)
    random_list = []
    for x in range(bran_inv):
        rand = random.choice(runner[_])
        random_list.append(rand)
        runner[_].remove(rand)

    big.append(random_list)


for _ in range(5):
    print(*big[_], sep='  {} \n'.format(name[_]))
