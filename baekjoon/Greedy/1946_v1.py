import sys

t = int(sys.stdin.readline())

for i in range(t):
  
  n = int(sys.stdin.readline())
  
  applicant = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
  not_employee = []
  
  for a in applicant:
    for b in applicant:
      if b[0] > a[0] and b[1] > a[1] and b not in not_employee:
        not_employee.append(b)

  print(len(applicant) - len(not_employee))