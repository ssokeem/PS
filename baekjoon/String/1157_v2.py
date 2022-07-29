word = input().upper()
spell = list(set(word))
dp = []

for i in spell:
  dp.append(word.count(i))
  
if dp.count(max(dp)) > 1:
  print("?")
else:
  print(spell[dp.index(max(dp))])