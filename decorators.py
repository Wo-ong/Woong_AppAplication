#
# # def decorator(func):
# #     def decorated(width, height):
# #         if width > 0 and height > 0:
# #             func(width, height)
# #         else:
# #             print("입력값 오류")
# #
# #       return decorated
# #
# # @decorator
# # def triangle(width, height):
# #     print("삼각형 넓이")
# #     print(width * height / 2)
# #
# # @decorator
# # def ractangle(width, height):
# #     print("사각형 넓이")
# #     print(width * height)
# #
# # width = int(input("가로 : "))
# # height = int(input("세로 : "))
# #
# # triangle(width, height)
# # ractangle(width, height)
#
# # 강사님 코드
# def check_integer(func):
#     def decorated(user, width, height):
#         if width >= 0 and height >= 0:
#             return func(user, width, height)
#         else:
#             raise ValueError('Input must be positive value')
#         return decorated
#
# def login_required(func):
#     def decorated(user, width, height):
#         if user.is_authenticated:
#             return func(user, width, height)
#         else:
#             raise PermissionError('login required')
#         return dacoreted
#
# @check_integer
# @login_required
# def rect_area(width, height):
#     return width * height
#
# @check_integer
# @login_required
# def tri_area(width, height):
#     return width * height / 2
#
#
# class User:
#     def __init__(self, auth):
#         self.is_authenticated = auth
#
# user = User(auth=False)
#
# r_area = rect_area(user, 10, 10)
# print(r_area)
# t_area = tri_area(user, 10, 10)
# print(t_area)