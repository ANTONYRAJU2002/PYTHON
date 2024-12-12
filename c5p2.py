print("Name : Antony raju\nRoll No : 15")
with open('c5p2in.txt', 'r') as source_file, open('c5p2out.txt', 'w') as target_file:
    for index, line in enumerate(source_file, start=1):
        if index % 2 != 0:
            target_file.write(line)
print("Odd lines have been copied to target.txt.")
