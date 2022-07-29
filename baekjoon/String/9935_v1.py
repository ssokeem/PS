word = input()
bomb = input()

while word.find(bomb) != -1:
  word = word[:word.find(bomb)] + word[word.find(bomb)+len(bomb):]
  if word == "":
    print("FRULA")
  elif word.find(bomb) == -1:
    print(word)
  else:
    pass