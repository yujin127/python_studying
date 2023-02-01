# # 1. Hello World!를 화면에 출력하는 문제
#
# print("Hello World!")
#
# # 2. 두 수를 입력받고 합을 출력하는 문제
# A, B = map(int, input().split())
# # print(A+B)
#
# # map 함수는 map(함수, 리스트(튜플 ...)) 형식으로 주어지고
# # 첫 번째 인수인 함수에 두 번째 인수인 리스트, 튜플 등을 반복적용하는 함수이다.
#
# # 3. 두 수를 입력받고 뺄셈을 한 결과를 출력하는 문제
# A, B = map(int, input().split())
# # print(A-B)
#
# # 4. 두 수를 입력받고 곱셈을 한 결과를 출력하는 문제
# A, B = map(int, input().split())
# # print(A*B)
#
# # 4. 두 수를 입력받고 나눗셈을 한 결과를 출력하는 문제
# A, B = map(int, input().split())
# # print(A/B)
#
# # 5. 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
# A, B = map(int, input().split())
# # print(A+B)
# # print(A-B)
# # print(A*B)
# # print(A/B)
# # print(A%B)

# 6. 가입하려고 하는 사이트에 이미 존재하는 아이디가 주어졌을 때, 놀람을 표현하는 프로그램을 작성하시오.
A = "joonas"
B = input("")
if A == B:
    print(A+"??!")