#Create a list of 5 fruits. Print the first and last fruit using indexing.(Concept: list, indexing)
#Add "Mango" to the list. Then remove the 2nd fruit.(Concept: list methods (append, pop, remove))

fruits_list=['apple','banana','grapes','peach','cherry']
print("first:",fruits_list[0])
print("last:",fruits_list[-1])

fruits_list.append('mango')
print("\n fruits list after add another fruit:",fruits_list)

fruits_list.remove(fruits_list[1])
print("\n fruits list after removal of 2nd fruit:",fruits_list)


fruits_list.pop(1)
print("\n fruits list after removal of 2nd fruit:",fruits_list)


