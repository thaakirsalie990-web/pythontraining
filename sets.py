st = set()
print(st)

st = {'item1', 'item2', 'item3', 'item4'}
print(st)

fruits = {'banana', 'apple', 'pineapple', 'orange'}
print(fruits)
print(len(fruits))

# ===================================================

print('item1 is in the set', 'item1' in st)

# ============================
st = {'item2'}
st.add('item1') # it set cannot be an empty set
print(st)

fruits.add('lime')
print(fruits)

# =====================================

st = {'item1', 'item2'}
st.update(['item3', 'item4']) # it inserts the items in the middle
print(st)

vegetables = ('tomato', 'carrot', 'choco')
fruits.update(vegetables)
print(fruits)

# ==========================================

st = {'item1', 'item2'}
st.remove('item2')
print(st)

# ==========================================

fruits = {'Watermelon', 'Banana', 'Orange', 'Choco'}
fruits.pop()
print(fruits) # randomly removes an item. if you print multiple times it will also be random

# the removed item
removed_item = fruits.pop()
print(removed_item)

# ===========================================
st = {'item1', 'item2', 'item3', 'item4'}
print(st)
st.clear() #basically empty
print(st)

fruits = {'melon', 'apple', 'banana', 'orange'}
print(fruits)
fruits.clear()
print(fruits)

# ============================================

st = {'item1', 'item2', 'item3', 'item4'}
print(st)
del st # it is not defined because it is deleted. tested it with print()

fruits = {'apple', 'banana', 'orange', 'guava'}
print(fruits)
del fruits # it is undefined

lst = ['item1', 'item2', 'item3', 'item4']
print(lst)
# set4 = set(lst) # why is this getting an error
# print(set4)

fruit_list = ['banana', 'apple', 'guava', 'melon']
print(fruit_list)

fruits_st = set(fruit_list) # something is weird why is it saying that this is not a callback function?
print(fruits_st) # figured out the issue. I created a variable with the label 'set' which caused the issue

# =================================================
# joining

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

fruits1 = {'choco', 'orange'}
fruits2 = {'melon', 'apple'}
fruits_st = fruits1.union(fruits2)
print(fruits_st)

fruits_1 = {'banana', 'appricot'}
fruits_2 = {'watermelon', 'peach'}
fruits_1.update(fruits_2)
print(fruits_1)

# =======================================================

st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st1.intersection(st2)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers)
print(whole_numbers) # is it supposed to print all the numbers

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
on = python.intersection(dragon) # figured it out
print(on)

# =========================================================

st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2'}
subset2 = st2.issubset(st1) # what does a subset or superset mean?
subset1 = st1.issuperset(st2)
print(subset2, subset1)


subset10 = whole_numbers.issubset(even_numbers)
superset10 = whole_numbers.issuperset(even_numbers)
print(subset10, superset10)

subset_strings = python.issubset(dragon)
print(subset_strings)

# =======================================================

st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2'}

d_st1 = st2.difference(st1)
d_st2 = st1.difference(st2)

print(d_st1, d_st2)

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}

python = python.difference(dragon)
dragon = dragon.difference(python)
print(python, dragon)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

d_numbers = whole_numbers.difference(even_numbers)
print(d_numbers)

# =====================================================

st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2'}

s_diff = st1.symmetric_difference(st2)
print(s_diff)

s_diff = whole_numbers.symmetric_difference(even_numbers)
print(s_diff)

# =========================================================

st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2'}

st2 = st2.isdisjoint(st1)
print(st2)

even_numbers = {0, 2, 4, 6, 8, 10}
odd_numbers = {0, 1, 3, 5, 7, 9}
check = even_numbers.isdisjoint(odd_numbers)
print(check)

check2 = odd_numbers.isdisjoint(even_numbers)
print(check2)
