'''Parašyti programą, kuri su eilute "Zen of Python" darytų šiuos veiksmus:
• Atspausdintų paskutinį antro žodžio simbolį
• Atspausdintų pirmą trečio žodžio simbolį
• Atspausdintų tik pirmą žodį
• Atspausdintų tik paskutinį žodį
• Atspausdintų visą frazę atbulai
• Atskirtų žodžius ir juos atspausdintų
• Žodį "Python" pakeistų į "Programming" ir atspausdintų naują sakinį
Patarimas: naudoti string karpymo įrankius, funkcijas split(), replace()
'''


s = "Zen of Python"
s_words = s.split()
print(s_words[1][len(s_words[1])-1])
print(s_words[2][0:1:])
print(s_words[0])
print(s_words[len(s_words)-1])
print(s[::-1])
print(s_words)
print(s.replace("Python", "Programming"))