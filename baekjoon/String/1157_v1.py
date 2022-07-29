spell = list(input().upper())
n = len(spell)
dp = [0] * n

for i in range(n):
  if dp[i] == 0:
    for j in range(i, n):
      if spell[i] == spell[j]:
        dp[i] += 1
        
max_list = [max(dp)==dp[i] for i in range(n)]

if max_list.count(True) > 1:
  print("?")
else:
  print(spell[max_list.index(True)])