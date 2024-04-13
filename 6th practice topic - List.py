#______________________________________________________________________________
#                                List
#------------------------------------------------------------------------------
# List items are ordered, changeable, and allow duplicate values.
# Lists are created using square brackets --> []:

mark = [95,98,100]
print (mark)
print (mark[0])
print (mark[1])
print (mark[2])
print (mark[-1])  # range could be in minus in python
print (mark[-2])
print (mark[-3])

print (mark[0:2])   # it is the range which we want to print of marks variable
print (mark[1:3])

                  # To add any number in list : append()
mark.append(99)
print (mark)

                 # To add any number in specific index : insert()
mark.insert(2,99)
print (mark)
                 # To check any number exsist or not :  in
print (99 in mark)

                # To check the length of the list : len()
print (len(mark))

#------------------------------------------------------------------------------
#                        for loop in list :
#------------------------------------------------------------------------------
for score in mark :
    print (score)

#_______________________________________________________________________________
#                 While loop in list
#-------------------------------------------------------------------------------

mark = [95 ,98, 97]

i=0
while i< len(mark):
    print (mark[i])
    i= i+1

#------------------------------------------------------------------------------
#                   Break & Continue
#------------------------------------------------------------------------------

students = ['ram','shyam','kishan','radha','radhika']

for student in students:
    if student == 'radha':
        break;              #fpr break keyword, loop will stop right there
    print (student)

for student in students :
    if student == 'kishan':
        continue;           #for continue keyword, loop will print all the elements except that one
    print(student)