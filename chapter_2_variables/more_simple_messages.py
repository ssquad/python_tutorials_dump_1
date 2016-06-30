#name variables
first_name1 = "kevin"
last_name1 = "buchanan"
first_name2 = "einat"
last_name2 = "korman"
first_name3 = "ayla"
last_name3 = "buchanan"
full_name1 = first_name1 + " " + last_name1
full_name2 = first_name2 + " " + last_name2
full_name3 = first_name3 + " " + last_name3
favorite_name = "Keren and John"

#messages to print
message_hello_1 = "Hello, " + full_name1.title() + "!"
print(message_hello_1)

message_hello_2 = "Hello, " + full_name2.title() + "!"
print(message_hello_2)

message_hello_3 = "Hello, " + full_name3.title() + "!"
print(message_hello_3)

message_howareyou_1 = first_name1.title() + ", how are you doing today?"
print(message_howareyou_1)


message_howareyou_2 = first_name2.title() + ", how are you doing today?"
print(message_howareyou_2)

message_howareyou_3 = first_name3.title() + ", how are you doing today?"
print(message_howareyou_3)

message_family_all = first_name1.title() + ", " + first_name2.title() + ", and " + first_name3.title() + " are a family."
print(message_family_all)

message_family_everyone = message_family_all + " They are very lucky to live with " + favorite_name + ", the most favorite of all family members."
print(message_family_everyone)
