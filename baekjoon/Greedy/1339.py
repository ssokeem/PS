import sys

n = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for _ in range(n)]

alphabet = []
count_dict = {}
result = 0

for word in word_list:
  for a in word:
    alphabet.append(a)
    
for a in set(alphabet):
  count_dict[a] = 0
  
for word in word_list:
  for i, a in enumerate(word):
    count_dict[a] += 10 ** (len(word) - i - 1)
    
sorted_values = sorted(count_dict.values(), reverse=True)

for i in range(len(sorted_values)):
  result += sorted_values[i] * (9 - i)

print(result)