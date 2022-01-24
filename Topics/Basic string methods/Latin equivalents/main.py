name = input()

def normalize(name):
    new_name = name.replace("é", "e")
    new_name = new_name.replace("ë", "e")
    new_name = new_name.replace("á", "a")
    new_name = new_name.replace("å", "a")
    new_name = new_name.replace("œ", "oe")
    new_name = new_name.replace("æ", "ae")
    return new_name

print(normalize(name))

# name = input()
#
#
# def normalize(text):
#     # put your code here
#     replacements = {
#         "é": "e",
#         "ë": "e",
#         "á": "a",
#         "å": "a",
#         "œ": "oe",
#         "æ": "ae",
#     }
#
#     for value in replacements:
#         text = text.replace(value, replacements.get(value))
#
#     return text
#
#
# print(normalize(name))