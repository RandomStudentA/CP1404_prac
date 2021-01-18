import os


def main():
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            pass

        extension = filename.split('.')[-1]
        if extension not in extension_to_category:
            category = input("What type would you like to sort your {} files into? ".format(extension))
            extension_to_category[extension] = category
            try:
                os.mkdir(category)
            except OSError:
                pass
        os.rename(filename, "{}/{}".format(extension_to_category[extension], filename))


main()