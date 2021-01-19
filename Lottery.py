import random

ID_Number = [316583145, 312797246, 316614882, 315997049]

first_question = 0
second_question = 0
third_question = 0
forth_question = 0
fifth_question = 0
sixth_question = 0

while first_question <= 0:
    first_question = ID_Number[random.randint(0, 3)] % random.randint(1, 9)

while second_question <= 10:
    second_question = ID_Number[random.randint(0, 3)] % random.randint(10, 17)

while third_question <= 18:
    third_question = ID_Number[random.randint(0, 3)] % random.randint(18, 29)

while forth_question <= 18 or forth_question == third_question:
    forth_question = ID_Number[random.randint(0, 3)] % random.randint(18, 29)

while fifth_question <= 30:
    fifth_question = (ID_Number[random.randint(0, 3)] % random.randint(30, 35)) + random.randint(0, 4)

while sixth_question <= 36:
    sixth_question = (ID_Number[random.randint(0, 3)] % random.randint(36, 41)) + random.randint(0, 4)

print("First quesion is:" + str(first_question))
print("Second quesion is:" + str(second_question))
print("Third quesion is:" + str(third_question))
print("Forth quesion is:" + str(forth_question))
print("Fifth quesion is:" + str(fifth_question))
print("Sixth quesion is:" + str(sixth_question))