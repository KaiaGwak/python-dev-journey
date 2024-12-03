# ===== 1. 변수 이름 규칙 =====
# 올바른 변수명
valid_name = "John"
age2 = 25
_private = "private variable"
firstName = "camelCase"  # camelCase도 가능하지만 Python에서는 snake_case 선호
first_name = "snake_case"  # Python 권장 스타일

# 잘못된 변수명 예시 (주석 해제하면 에러 발생)
# 2name = "John"     # 숫자로 시작할 수 없음
# my-name = "John"   # 하이픈 사용 불가
# class = "Python"   # 예약어 사용 불가

# ===== 2. 다중 할당 =====
# 여러 변수에 같은 값 할당
x = y = z = 0
print(f"x: {x}, y: {y}, z: {z}")

# 여러 변수에 다른 값 할당
a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")

# 값 교환하기
a, b = b, a
print(f"교환 후 - a: {a}, b: {b}")

# ===== 3. 변수 타입 =====
# 기본 데이터 타입
integer_var = 100
float_var = 3.14
string_var = "Hello"
boolean_var = True
none_var = None

print("\n변수 타입:")
print(f"integer_var: {type(integer_var)}")
print(f"float_var: {type(float_var)}")
print(f"string_var: {type(string_var)}")
print(f"boolean_var: {type(boolean_var)}")
print(f"none_var: {type(none_var)}")

# ===== 4. 변수 스코프 =====
global_var = "전역 변수"

def scope_test():
    local_var = "지역 변수"
    print(f"\n함수 내부에서:")
    print(f"지역 변수 접근: {local_var}")
    print(f"전역 변수 접근: {global_var}")

scope_test()
print(f"\n함수 외부에서:")
print(f"전역 변수 접근: {global_var}")
# print(f"지역 변수 접근: {local_var}")  # 에러 발생: local_var는 함수 외부에서 접근 불가

# ===== 5. 특별한 변수 규칙 =====
# 언더스코어 변수
_private = "비공개 변수 관례"
__very_private = "매우 비공개 변수"
normal_var = "일반 변수"

# ===== 6. 상수 (파이썬은 진정한 상수가 없지만 관례적으로 사용) =====
MAX_VALUE = 100  # 대문자로 작성하여 상수임을 나타냄
PI = 3.14159

# ===== 7. f-strings (Python 3.6+) =====
name = "Alice"
age = 25
print(f"\n{name}는 {age}살입니다.")

# ===== 8. 변수 삭제 =====
temp_var = "임시 변수"
del temp_var
# print(temp_var)  # 에러 발생: 변수가 삭제됨

# 실습 예제
def practice_example():
    # 1. 여러분의 이름과 나이를 변수에 저장하세요
    # 2. f-string을 사용하여 자기소개를 출력하세요
    # 3. 다중 할당을 사용하여 세 과목의 점수를 저장하세요
    # 4. 변수의 값과 타입을 모두 출력해보세요
    pass  # 여기에 코드를 작성하세요