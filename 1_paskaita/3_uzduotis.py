'''Programoje išbandyti daugiau string funkcijų:
• upper()
• casefold()
• capitalize()
• count()
• find()
• ir t.t.
Visas jas galite rasti čia: https://www.w3schools.com/python/python_ref_string.asp '''

s = "Zen of Python"
s_words = s.split()
print(s_words[1][len(s_words[1])-1])
print(s_words[2][0:1:])
print(s_words[0])
print(s_words[len(s_words)-1])
print(s[::-1])
print(s_words)
print(s.replace("Python", "Programming"))


print(s.upper())
print(s.casefold())
print("Raide e tekste pasikartoja {} kartu".format(s.count("e")))