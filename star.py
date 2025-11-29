n = int(input("별의 층 입력: ")
star = 0
for i in range(n + 1):
    print("*" * i)
    star += i
print("\n")
print("별의 총 개수:", star, "개")
