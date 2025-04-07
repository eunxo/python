for dan in range(2, 10):
    print(f"  {dan}단", end="\t")
print()

# 구구단 내용 출력
for i in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan} x {i} = {dan * i:2}", end="\t")
    print()
    