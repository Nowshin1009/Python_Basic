score = input("Enter your score : ")
score=int(score)
if 90<=score<=100 :
    grade = "A"
elif 80<=score<=89 :
    grade = "B"
elif 70<=score<=79 :
    grade = "C"
elif 60<=score<=69 :
    grade = "D"
elif 50<=score<=59 :
    grade = "E"
elif 40<=score<=49 :
    grade = "E-"
else :
    grade = "F"

print(grade)