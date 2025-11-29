major = input("학과(전공) 입력: ")
id = input("학번 입력: ")
name = input("이름 입력: ")
subject = int(input("점수 입력할 교과목 개수 입력: "))
score = []
sum = 0

for i in range(subject):
  s = int(input(str(i + 1) + "번째 점수 입력:"))
  score.append(s)
  sum += score[i]

average = sum / subject

print("교과목 수:", subject)
print("평균:", average)
