#Create some sets and illustrate how to operate them

S1={1,2,3,1}
S2={2,4,6}

print('Here is S1')
print(S1)
print('Here is S2')
print(S2)

# Typical set lperations as differnce and union
diff=S1.difference(S2)

print('diff')
print(diff)

un=S1.union(S2)
print('Union')
print(un)

# Set operators can be used as an alternative to the method calls
# above.
print("S1: ", S1)
print("S2: ", S2)

opDiff = S1 - S2
print ("Difference: S1 - S2: ", opDiff)
opDiff = S2 - S1
print("Difference: S2-S1: ", opDiff)

intersect = S1 & S2
print("Intersection: ", intersect)

union = S1 | S2
print("Union: ", union)

# Make sets of diverse types and test how the basic set operations work
print("==========================================================")
S3={'per', 2, 'b', 4}
print("S3: ", S3)
S4={1, 5, 'kul', 's', 'per', 'b'}
print("S4: ", S4)
unionS3S4 = S3 | S4
print("S3 UNION S4: ", unionS3S4)
intersectS3S4 = S3 & S4
print("S3 INTERSECT S4: ", intersectS3S4)
diffS3S4 = S3-S4
print("S3-S4: ", diffS3S4)
diffS4S3 = S4-S3
print("S4-S4: ", diffS4S3)
