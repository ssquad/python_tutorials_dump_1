
#lists [ ] with commas to separate
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#index of list starts at 0
#first item in list is in position 0
#-index number counts position from the end of list
print(bicycles[0])
print(bicycles[0].upper())

print(bicycles[1].title())
print(bicycles[3])
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)

#practice lists - names
names_family_korman = ['zeev', 'dina', 'keren', 'einat', 'yael']
names_family_buchanan = ['walter', 'linda', 'michael', 'kevin']
print(names_family_korman[0].title())
print(names_family_korman[1].title())
print(names_family_korman[2].title())
print(names_family_korman[3].title())
print(names_family_buchanan[0].title())
print(names_family_buchanan[1].title())
print(names_family_buchanan[2].title())


names_family_korman_buchanan = [names_family_korman[3], names_family_buchanan[3], 'ayla']
print(names_family_korman_buchanan)

family_message = "Happy family Korman Buchanan:\t" + str(names_family_korman_buchanan[0].title()) + ", " + str(names_family_korman_buchanan[1].title()) + ", " + str(names_family_korman_buchanan[2].title())
print(family_message)


#me exploring numbers 
numbers = [1, 3, 5, 7, 9]
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

print(numbers[0:3])
print((numbers[0:3])*3)
numbers_multiply = numbers * 3
print(numbers_multiply)

#how do I operate on a list?


#changing element in an existing list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#append element to an existing list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)


numbers = [1, 3, 5, 7, 9]
print(numbers)
numbers.append(11)
print(numbers)


motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

#del statment to delete element from an existing list
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)
motorcycles.insert(1, 'harley')
print(motorcycles)

#pop removes last item in a list but allows you to work on it after removing
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#popping an item from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#remove allows you to remove an item based on value not position
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#can you describe a value (like odd) to remove all items that meet the criteria?
numbers = [1,2,3,4,5]
print(numbers)
numbers.remove(3) #here I want to describe a condition or criteria like ODD
print(numbers)

#using remove to work on element removed
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

#remove only removes first element with the value - if more than one element exists in a list, need to run a loop
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 1, 3, 2]
print(numbers)
numbers.remove(3)
print(numbers)

#guest list
guests = ['Zeev Korman', 'Igor Stravinsky', 'Nikolai Tesla']
invitation = guests[0] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to seeing you again."
print(invitation)
invitation = guests[1] + ", you and a guest are cordially invited to dinner this evening, June 26, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)
invitation = guests[2] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)


#remove guest from list, print name of guest not attending 

guest_notattending_1 = 'Igor Stravinsky'
guests.remove(guest_notattending_1)
guests.insert(1, 'Billie Holiday')
print(guests)

guest_notattending_2 = guests.pop(2)
print(guests)
print("\n")
guests.insert(2, 'Virginia Wolf')
print(guests)

#print invitation to guests, print message with names of those that cannot attend
invitation = guests[0] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to seeing you again."
print(invitation)
invitation = guests[1] + ", you and a guest are cordially invited to dinner this evening, June 26, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)
invitation = guests[2] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)

print(guest_notattending_1 + " and guest will not be able to attend.")
print(guest_notattending_2 + " and guest will not be able to attend.")

print(guests)
print("\n")

#add invitees
invitation = "Great news, " + guests[0] + ", we found a bigger table and will be able to invite MORE friends!"
print(invitation)
invitation = "Great news, " + guests[1] + ", we found a bigger table and will be able to invite MORE friends!"
print(invitation)
invitation = "Great news, " + guests[2] + ", we found a bigger table and will be able to invite MORE friends!"
print(invitation)

guests.insert(0, 'Eva Cassidy')
guests.insert(2, 'Eleanor Roosevelt')
guests.append('Prince')

print("\n")
print(guests)
print("\n")

#invitations for those that are on expanded guest list
invitation = guests[1] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to seeing you again."
print(invitation)
invitation = guests[0] + ", you and a guest are cordially invited to dinner this evening, June 26, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)
invitation = guests[2] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)
invitation = guests[3] + ", you and a guest are cordially invited to dinner this evening, June 26, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)
invitation = guests[4] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)
invitation = guests[5] + ", you and a guest are cordially invited to dinner this evening, June 25, 2016, at 8 o'clock. We look forward to meeting you both."
print(invitation)

#remove all but two guests; message popped guests, confirm invitations for remaining guests
guests.remove('Eleanor Roosevelt')
guests[0] = 'Eleanor Roosevelt'
print(guests)
print("\n")

guests.append('Eva Cassidy')
print("\n")
print(guests)
print("\n\n")

message_to_guests = "Dear " + guests[0] + ", \n\nUnfortunately, our new table will not arrive in time for the dinner, and we can only accommodate two people for dinner.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(message_to_guests)
message_to_guests = "Dear " + guests[1] + ", \n\nUnfortunately, our new table will not arrive in time for the dinner, and we can only accommodate two people for dinner.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(message_to_guests)
message_to_guests = "Dear " + guests[2] + ", \n\nUnfortunately, our new table will not arrive in time for the dinner, and we can only accommodate two people for dinner.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(message_to_guests)
message_to_guests = "Dear " + guests[3] + ", \n\nUnfortunately, our new table will not arrive in time for the dinner, and we can only accommodate two people for dinner.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(message_to_guests)
message_to_guests = "Dear " + guests[4] + ", \n\nUnfortunately, our new table will not arrive in time for the dinner, and we can only accommodate two people for dinner.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(message_to_guests)
message_to_guests = "Dear " + guests[5] + ", \n\nUnfortunately, our new table will not arrive in time for the dinner, and we can only accommodate two people for dinner.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(message_to_guests)


print("\n")
print(guests)
message_to_pop_guests = "Dear " +  guests.pop() + ", \n\nUnfortunately, we can no longer accommodate you and your guest for dinner. We hope to reschedule in the near future.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(guests)
print(message_to_pop_guests)

print("\n")
print(guests)
message_to_pop_guests = "Dear " +  guests.pop() + ", \n\nUnfortunately, we can no longer accommodate you and your guest for dinner. We hope to reschedule in the near future.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(guests)
print(message_to_pop_guests)

print("\n")
print(guests)
message_to_pop_guests = "Dear " +  guests.pop() + ", \n\nUnfortunately, we can no longer accommodate you and your guest for dinner. We hope to reschedule in the near future.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(guests)
print(message_to_pop_guests)

print("\n")
print(guests)
message_to_pop_guests = "Dear " +  guests.pop() + ", \n\nUnfortunately, we can no longer accommodate you and your guest for dinner. We hope to reschedule in the near future.\n\nOur sincere apologies,\n\nThe Korman Buchanans"
print(guests)
print(message_to_pop_guests)

message_to_invited_guests = "Dear " + guests[1] + ", \n\nFortunately, we can still accommodate you and your guest for dinner. We hope to reschedule with others in the near future, and look forward to seeing you tonight! \n\nWe look forward to catching up!\n\nThe Korman Buchanans"
print(message_to_invited_guests)
message_to_invited_guests = "Dear " + guests[0] + ", \n\nFortunately, we can still accommodate you and your guest for dinner. We hope to reschedule with others in the near future, and look forward to seeing you tonight! \n\nWe look forward to meeting you and your guest!\n\nThe Korman Buchanans"
print(message_to_invited_guests)

#delete remaining two guests, check list to confirm it is empty
print("\n")
print(guests)
del guests[0]
print(guests)
del guests[0]
print(guests)

