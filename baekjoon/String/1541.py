split_str = input().split("-")

for i, str in enumerate(split_str):
  
  if str.find("+") != -1:
    plus_list = str.split("+")
    plus_list_a = map(int, plus_list)  
    split_str[i] = sum(plus_list_a)
      
num_list = list(map(int, split_str))
total = num_list[0]
num_list.pop(0)

for num in num_list:
  total -= num
  
print(total)