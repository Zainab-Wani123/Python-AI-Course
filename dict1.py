#Create a dictionary of 3 students and their scores. Print each student and score using a loop.(Concept: dictionary, for loop, items())
student_data={'1':350,'2':300,'3':400}
'''for i ,score in student_data.items():
   print(i,"scored",score)'''
for i in student_data.keys():
    print(i,"scored",student_data[i])

for score in student_data.values():
    print("score:",score)

#student_data['4']=500 
student_data.update({'4':500})
print("students_data dictionary updation:",student_data)

