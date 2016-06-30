#APOSTROPHES AND QUOTES
message = "One of Python's strengths is its diverse community."
print(message)

#Changed the quotes on this, otherwise, file wouldn't run
#You can wrap single quotes within double quotes
# Was message = 'One of Python's strengths is its diverse community.'
message = "One of Python's strengths is its diverse community."
print(message)

#NAMES APOSTROPHES AND QUOTES
print('Arthur Schopenhauer said, "All truth passes thorugh three stages. First, it is ridiculed. Second, it is violently opposed. Third, it is accepted as being self-evident."')

philosopher_1 = "Rene Descartes"
philosopher_2 = "David Hume"
philosopher_3 = "Georg Wilhelm Friedrick Hegel"

quote_1 = "Divide each difficulty into as many parts as is feasible and necessary to resolve it."
quote_2 = "Generally speaking, the errors in religion are dangerous; those in philosophy only ridiculous."
quote_3 = "An idea is always a generalization, and generalization is a property of thinking. To generalize means to think."


print(philosopher_1 + " once said, " + '"' + quote_1 + '"')
print(philosopher_2 + " once said, " + '"' + quote_2 + '"')
print(philosopher_3 + " once said, " + '"' + quote_3 + '"')

message_quote_1 = philosopher_1 + " once said, " + '"' + quote_1 + '"'
message_quote_2 = philosopher_2 + " once said, " + '"' + quote_2 + '"'
message_quote_3 = philosopher_3 + " once said, " + '"' + quote_3 + '"'

print(message_quote_1)
print(message_quote_2)
print(message_quote_3)

#MORE STRIP 
philosopher_1_ws = " \t Rene \t Descartes "
print(philosopher_1_ws)
print(philosopher_1_ws.lstrip())
print(philosopher_1_ws.rstrip())
print(philosopher_1_ws.strip())
print(philosopher_1_ws.replace("\t", "").replace(" ", "").strip())
print(philosopher_1_ws.strip())


