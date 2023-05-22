def get_name_value(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

def main():
    # Read the names from the file and store them in a list
    with open("names.txt", "r") as file:
        names = file.read().replace('"', '').split(',')

    # Sort the names alphabetically
    names.sort()

    # Calculate the total of all the name scores in the list
    total_name_scores = sum((i + 1) * get_name_value(name) for i, name in enumerate(names))

    print("The total of all the name scores in the file is:", total_name_scores)

if __name__ == "__main__":
    main()
