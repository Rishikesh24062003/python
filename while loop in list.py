#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rishi
#
# Created:     10/01/2023
# Copyright:   (c) rishi 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
students = ["ram","shyam","kishan","radha","radhika"]

for student in students:
    if student == "radha":
        break;
    print(student)

for student in students:
    if student == "kishan":
        continue;
    print(student)

