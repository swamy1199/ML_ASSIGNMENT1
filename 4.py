it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')
print(it_companies)

it_company = {'TCS','Wipro','Infosys'}
it_companies.update(it_company)
print(it_companies)

it_companies.remove('Wipro')
print(it_companies)

C = A.union(B)
print(C)

D = A.intersection(B)
print(D)

print(A.issubset(B))

print(A.isdisjoint(B))

E = A.union(B)
print(E)
F = B.union(A)
print(F)

sym = A.symmetric_difference(B)
print(sym)

del A
del B
del it_companies

set_ages = set(age)
print(set_ages)

print(len(age))
print(len(set_ages))