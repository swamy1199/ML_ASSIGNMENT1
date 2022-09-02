it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Finding the length of the set it_companies
print(len(it_companies))
# Adding 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)
# Inserting multiple IT companies at once to the set it_companies
it_company = {'TCS','Wipro','Infosys'}
it_companies.update(it_company)
print(it_companies)
# Removing one of the companies from the set it_companies
it_companies.remove('Wipro')
print(it_companies)
# Difference between remove and discard
# In discard () method, if the element is not present in the set, it does not throw any exception, wherein remove () method if the element is not present in the set, it throws an exception.
# Joining A and B, assigning it to C
C = A.union(B)
print(C)
# Instersecting A and B, assigning it to D
D = A.intersection(B)
print(D)
# Checking weather A is subset of B or Not
print(A.issubset(B))
# Checking weather A and B are disjoint or Not
print(A.isdisjoint(B))
# Joining A with B and B with A
E = A.union(B)
print(E)
F = B.union(A)
print(F)
# Finding symmetric difference between A and B
sym = A.symmetric_difference(B)
print(sym)
# Deleting the sets Completely
del A
del B
del it_companies
# Converting the list to a set
set_ages = set(age)
print(set_ages)
# Comparing the length of the list and the set.
print(len(age))
print(len(set_ages))