# control_flow.py

# ===== 1. if-elif-else 조건문 =====
def check_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# 성적 확인
score = 85
grade = check_grade(score)
print(f"점수: {score}, 학점: {grade}")

# ===== 2. for 반복문 =====
# 기본 for 문
print("\n1부터 5까지 출력:")
for i in range(1, 6):
    print(i, end=" ")

# 리스트 순회
fruits = ["사과", "바나나", "오렌지"]
print("\n\n과일 목록:")
for fruit in fruits:
    print(fruit, end=" ")

# enumerate 사용
print("\n\n번호가 있는 과일 목록:")
for index, fruit in enumerate(fruits, 1):
    print(f"{index}. {fruit}")

# ===== 3. while 반복문 =====
print("\nwhile 반복문:")
count = 0
while count < 3:
    print(f"카운트: {count}")
    count += 1

# ===== 4. break와 continue =====
print("\nbreak 예제:")
for i in range(1, 6):
    if i == 3:
        break
    print(i, end=" ")

print("\n\ncontinue 예제:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i, end=" ")

# ===== 5. 중첩 반복문 =====
print("\n\n구구단 2단:")
for i in range(2, 3):
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")

# ===== 실습 예제 =====
def practice_control_flow():
    """
    1. 1부터 10까지의 숫자 중 짝수만 출력하기
    2. 리스트 [1, 2, 3, 4, 5]의 모든 요소를 2배로 만들기
    3. while문을 사용해서 1부터 시작하여 100을 넘지 않는 모든 7의 배수 출력하기
    4. 다음 리스트에서 음수는 제외하고 양수만 출력하기: [-5, 2, 0, -3, 4, -1, 6]
    """
    # 여기에 코드를 작성하세요
    pass

# ===== 6. match-case (Python 3.10+) =====
def get_day_type(day):
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            return "Weekday"
        case "saturday" | "sunday":
            return "Weekend"
        case _:
            return "Invalid day"

# 테스트
print(f"\n'Monday'는 {get_day_type('Monday')}")
print(f"'Sunday'는 {get_day_type('Sunday')}")