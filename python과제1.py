#인치를 센티미터로 변환
inch = float(input("inch>"))
cm = inch * 2.54
print(f"{inch}인치는 {cm}센티미터입니다")
#킬로그램을 파운드로 변환환
kg = float(input("kg>"))
pounds = kg * 2.20462
print(f"{kg}킬로그램은 {pounds}파운드입니다.")
#원의 반지름을 이용해 원의 둘레와 넓이 계산산
r = float(input("r>"))
circumference = 2 * r * 3.14159
area = r * r * 3.14159
print(f"원의둘레는{circumference},원의 넓이는{area}입니다")
