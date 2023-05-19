'''Sukurti programą, kuri:
• Prie kiekvieno sakinio su jūsų pasirinktu tekstu, pridėtų šauktuką ir atspausdintų naują sakinį.

Patarimai:
• Naudoti map (su lambda) arba comprehension, " ".join()'''

txt = "Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, " \
      "designed to perform well on many kinds of real-world data. It was invented by Tim Peters " \
      "in 2002 for use in the Python programming language. The algorithm finds subsets of the data that " \
      "are already ordered, and uses the subsets to sort the data more efficiently."

new_txt = map(lambda x: x + "!", txt.split('.'))
print(new_txt)
print(" ".join(new_txt))
# ---------------ARBA------------------------------------------------------------
new_txt = [x + "!" for x in txt.split('.')]
print(" ".join(new_txt))
