# functions.py

# ===== 1. 기본 함수 정의와 호출 =====
def greet(name):
    """
    사용자의 이름을 받아 인사를 출력하는 함수
    """
    return f"안녕하세요, {name}님!"

# 함수 호출
print(greet("Python"))

# ===== 2. 매개변수와 반환값 =====
def calculate_rectangle_area(width, height):
    """
    사각형의 넓이를 계산하는 함수
    """
    area = width * height
    return area

# 면적 계산
print(f"\n사각형의 넓이: {calculate_rectangle_area(5, 3)}")

# ===== 3. 기본 매개변수 =====
def power(base, exponent=2):
    """
    base의 exponent 제곱을 계산하는 함수
    기본값으로 제곱(2제곱)을 계산
    """
    return base ** exponent

print(f"\n2의 제곱: {power(2)}")        # 기본값 사용
print(f"2의 3제곱: {power(2, 3)}")      # 사용자 지정 값

# ===== 4. 가변 인자 (*args) =====
def sum_all(*numbers):
    """
    여러 숫자를 받아서 합계를 반환하는 함수
    """
    return sum(numbers)

print(f"\n합계: {sum_all(1, 2, 3, 4, 5)}")

# ===== 5. 키워드 인자 (**kwargs) =====
def print_info(**info):
    """
    키워드 인자를 받아 정보를 출력하는 함수
    """
    for key, value in info.items():
        print(f"{key}: {value}")

print("\n사용자 정보:")
print_info(name="Python", age=30, city="Seoul")

# ===== 6. 람다 함수 =====
square = lambda x: x**2
numbers = [1, 2, 3, 4, 5]
squared = list(map(square, numbers))
print(f"\n제곱한 리스트: {squared}")

# ===== 7. 함수 안의 함수 (중첩 함수) =====
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(f"\n5 더하기: {add_five(3)}")  # 8 출력

# ===== 실습 예제 =====
def practice_functions():
    """
    1. 두 수를 받아 사칙연산을 모두 수행하는 함수 만들기
    2. 가변 인자를 받아 최대값과 최소값을 반환하는 함수 만들기
    3. 람다 함수를 사용해서 리스트의 모든 요소에 3을 곱하기
    4. 재귀 함수를 사용해서 팩토리얼 계산하기
    """
    pass  # 여기에 코드를 작성하세요
