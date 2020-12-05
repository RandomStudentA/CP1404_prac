FILENAME = "subject_data.txt"


def main():
    data = get_data()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        message_print(input_file)
    input_file.close()


def message_print(input_file):
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # the data is split into 3 parts, the [] calls for certain parts only
        print(parts[0] + "is taught by " + parts[1] + " and has " + parts[2] + " students")


main()
