def count_and(filename):
    count = 0
    try:
        with open(filename, 'r') as f:
            for line in f:
                lower_line=line.lower()
                count += lower_line.count("and")

        print("Number of occurrences of 'AND':", count)
    except FileNotFoundError:
        print("File not found.")

# Driver code
count_and("STORY.txt")