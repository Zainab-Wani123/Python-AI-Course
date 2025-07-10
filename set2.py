#Find the union and intersection of two sets: {1,2,3} and {2,3,4}(Concept: set operations (union, intersection))
set1={1,2,3}
set2={2,3,4}

#union_set = set1.union(set2)
#print("Union:", union_set)
union= set1 | set2
print("union of sets:",union)

#intersection_set = set1.intersection(set2)
#print("Intersection:", intersection_set)
intersection=set1 & set2
print("intersection of sets:",intersection)