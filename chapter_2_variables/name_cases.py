first_name = "\tAyla"
middle_name = "\n\tSery"
last_name = "\n\tBuchanan"
full_name = first_name + " " + middle_name + " " + last_name
full_name_strip = first_name.strip() + " " + middle_name.strip() + " " + last_name.strip()
print(first_name)
print(middle_name)
print(last_name)
print("\ndone\n")

print(full_name)
print(full_name.upper())
print(full_name.lower())
print("\nfull_name_nostrip_done\n")

full_name = full_name_strip
print(full_name)
print(full_name.upper())
print(full_name.lower())
print("\nfull_name_strip_done\n")


first_name = first_name.strip()
middle_name = middle_name.strip()
last_name = last_name.strip()

full_name_list_title = "\tFIRST:\t\t" + first_name.title() + "\n\tMIDDLE:\t\t" + middle_name.title() + "\n\tLAST:\t\t" + last_name.title()
print(full_name_list_title)

full_name_list_upper = "\tFIRST:\t\t" + first_name.upper() + "\n\tMIDDLE:\t\t" + middle_name.upper() + "\n\tLAST:\t\t" + last_name.upper()
print(full_name_list_upper)


print(full_name.strip())
