#Read the file line-by-line and print each line with its line number.(Concept: readlines(), enumerate())
with open("notes.txt" ,"r") as file:
    lines=file.readlines()
    for line_number,line in enumerate(lines,start=1):
     print("line",line_number,':' ,"",line)

