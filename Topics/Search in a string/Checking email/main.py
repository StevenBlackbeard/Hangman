# def check_email(string):
#     out_dot = False
#     out_space = " " not in string
#     out_test = "@." not in string
#     out_at = "@" in string
#     if out_at:
#         idx = string.find("@") + 1
#         out_dot = string.find(".", idx) != -1
#     output = out_space and out_at and out_test and out_dot
#     return output

def check_email(string: str):
    if '@' in string and ' ' not in string and '@.' not in string:
        if string.index('@') < string.rfind('.'):
            return True
    return False
