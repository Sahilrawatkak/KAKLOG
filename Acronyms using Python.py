I = str(input("Enter a Phrase: "))
Text = I.split()
a=" "
for i in Text:
    a = a+str(i[0]).upper()
print(a)
