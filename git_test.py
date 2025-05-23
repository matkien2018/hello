"""
Test 1
Test 2 from work laptop
"""
additional_info = "Binh Le"
msg = f' Hello World! {additional_info}'
print(msg)

emails = ["first1.last1@company.com","first2.last2@company.com","first3.last3@company.com"]
for email in emails:
    print(email.split('@')[0])
    print(email.split('.')[0])

data = [(1,'ignore1','ignore2',1),(2,'ignore1','ignore2',2),(3,'ignore1','ignore2',3)]
for id, *_,dat in data:
    print(id, dat)

fruits = ["apple", "mango", "strawberry", "cherry", "peach","peach pie"]
allergies = ["cherry", "peach"]
okay = [fruit for fruit in fruits if not any(allergy in fruit.split() for allergy in allergies)]
print(okay)

add_one = lambda x: x + 1
print(f' lambda add_one(5) return %s' % add_one(5))