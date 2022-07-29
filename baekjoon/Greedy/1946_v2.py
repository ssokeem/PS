import sys

t = int(sys.stdin.readline())

for i in range(t):
  
  n = int(sys.stdin.readline())
  applicant = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)])
  
  top = 0
  employee_num = 1
  
  for j in range(len(applicant)):
    if applicant[j][1] < applicant[top][1]:
      top = j
      employee_num += 1
  
  print(employee_num)