COLOR_TO_NAME = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "azure1": "#f0ffff",
                 "beige": "#f5f5dc", "bisque1": "	#ffe4c4", "black": "#000000"}

color_name = input("Enter color name: ")
while color_name != "":
    if color_name in COLOR_TO_NAME:
        print(color_name, "is", COLOR_TO_NAME[color_name])
    else:
        print("Invalid color name")
    color_name = input("Enter color name: ")