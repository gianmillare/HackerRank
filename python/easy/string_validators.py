# def string_validators(x):
#     alphanum = []
#     alpha = []
#     digits = []
#     lowercase = []
#     uppercase = []
#
#     x = list(x)
#     results = []
#
#     for i in x:
#         if i.isalnum():
#             alphanum.append('true')
#         else:
#             alphanum.append('false')
#
#     for i in x:
#         if i.isalpha():
#             alpha.append('true')
#         else:
#             alpha.append('false')
#
#     for i in x:
#         if i.isdigit():
#             digits.append('true')
#         else:
#             digits.append('false')
#
#     for i in x:
#         if i.islower():
#             lowercase.append('true')
#         else:
#             lowercase.append('false')
#
#     for i in x:
#         if i.isupper():
#             uppercase.append('true')
#         else:
#             uppercase.append('false')
#
#     if 'true' in alphanum:
#         print('True')
#
#     if 'true' in alpha:
#         print('True')
#
#     if 'true' in digits:
#         print('True')
#
#     if 'true' in lowercase:
#         print('True')
#
#     if 'true' in uppercase:
#         print('True')
#
#
s = 'qA2'
# string_validators(s)

# SOLUTION
print(any(i.isalnum() for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))


