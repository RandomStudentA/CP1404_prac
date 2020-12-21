from prac_06.programming_language import ProgrammingLanguage

java = ProgrammingLanguage("Java", "Static", True, 1995)
cplusplus = ProgrammingLanguage("C++", "Static", False, 1982)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)


languages = [java, cplusplus, python, visual_basic, ruby]
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.field)