'''
#.sort() and .sort(reverse=True) - permanently sorts list order (alphabetically/chronologically)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']

numbers = [3, 1, 2, 5, 7, 9, 3, 0]
print(numbers)
numbers.sort()
print(numbers)
numbers = [3, 1, 2, 5, 7, 9, 3, 0]
numbers.sort(reverse=True)
print(numbers)

#.sorted() - temporarily sorts list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:\t\t" + str(cars))
print("\nHere is the sorted list:\t\t" + str(sorted(cars)))
print("\nHere is the original list again:\t" + str(cars))
#pg48 sorted() it says that it can accept a reverse=True argument,
#I have tried many different ways to write that all with errors:
#not sure how to phrase this statment to get a reverse temporarily ordered list


#.reverse() - permanently orders a list in reverse order
#(not numerically or alphabetically but whatever order the lsit is already in)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#len() - length of list
cars = ['bmw', 'audi', 'toyota', 'subaru']
length_cars = len(cars)
print(length_cars)

#practice - seeing the world pg50
dream_board_travel = ['italy', 'new zealand', 'ireland', 'scotland', 'poland','morrocco', 'turkey', 'brazil', 'gabon', 'alaska', 'galapagos islands']
print(dream_board_travel)
print("Here is the original list:\t\t" + str(dream_board_travel))
print("Here is the sorted list:\t\t" + str(sorted(dream_board_travel)))
print("Here is the orginal list again:\t\t" + str(dream_board_travel))
#again asking to temporarily reverse sort the list use sorted() with a reverse=True argument, cannot get that to work

    #print(dream_board_travel.sorted(reverse=True))
    #AttributeError: 'list' object has no attribute 'sorted'

    #print(sorted(dream_board_travel(reverse=True)))
    #TypeError: 'list' object is not callable

    #tried other ways = most are invalid syntax error so won't run)

dream_board_travel = ['italy', 'new zealand', 'ireland', 'scotland', 'poland','morrocco', 'turkey', 'brazil', 'gabon', 'alaska', 'galapagos islands']
print("Here is the original list:\t\t" + str(dream_board_travel))
dream_board_travel.reverse()
print("Here is the list in reverse order:\t" + str(dream_board_travel))
dream_board_travel.reverse()
print("here is the list reversed again, back to original:\t" + str(dream_board_travel))



dream_board_travel = ['italy', 'new zealand', 'ireland', 'scotland', 'poland','morrocco', 'turkey', 'brazil', 'gabon', 'alaska', 'galapagos islands']
print(dream_board_travel)
dream_board_travel.sort()
print(dream_board_travel)
dream_board_travel.sort(reverse=True)
print(dream_board_travel)


#guest list - length
guests = ['Eleanor Roosevelt', 'Zeev Korman', 'Billie Holiday', 'Virginia Wolf', 'Prince', 'Eva Cassidy']
print(guests)
print("Number of invited guests:\t" + str(len(guests)))
'''
#more practice trees
#all list functions
'''
replacing element in a list
list.append
list.insert(index, object)
del list[index]
list.pop([index])
list.remove(object)
list.sort() / list.sort(reverse=True)
sorted(list)
list.reverse()
len(list)
'''
trees = ['oak', 'maple', 'pine', 'cypress', 'elm', 'beech', 'birch', 'cherry', 'willow', 'cedar', 'redwood', 'walnut', 'peach', 'almond', 'apple']
print(trees)
print(len(trees))

#switch maple with japanese maple
trees[1] = 'japanese maple'
print(trees)

#append maple to end of list
trees.append('maple')
print(trees)
print(len(trees))

#insert new item fig to index position 0
trees.insert(0,'fig')
print(trees)
print(len(trees))

#pop last item off and print popped item and new list length
popped_trees = trees.pop()
print(popped_trees)
print(trees)
print(len(trees))

#pop item from index position 2 and print popped item and new list length
popped_trees = trees.pop(2)
print(popped_trees)
print(trees)
print(len(trees))

#insert maple and japanese maple back into list, remove japanese maple from list
trees.insert(0,'maple')
trees.append('japanese maple')
print(trees)

#remove japanese maple
trees.remove('japanese maple')
print(trees)

#sort functions
trees.sort()
print(trees)
trees.sort(reverse=True)
print(trees)

#sorted function- again cannot figure out how to reverse list temporarily
trees = ['maple', 'fig', 'oak', 'pine', 'cypress', 'elm', 'beech', 'birch', 'cherry', 'willow', 'cedar', 'redwood', 'walnut', 'peach', 'almond', 'apple', 'japanese maple']
print(trees)
print(sorted(trees))
print(trees)
print(sorted(trees,reverse=True))
import time
time.sleep(5)
print("NOW THAT'S ALL SORTED!")

#reverse function
trees.reverse()
print(trees)
trees.reverse()
print(trees)

trees.sort()
print(trees)
trees.reverse()
print(trees)

