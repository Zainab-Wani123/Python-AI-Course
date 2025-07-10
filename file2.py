#Use a with open() block to read from notes.txt and print the content.(Concept: context manager, read())
with open("notes.txt","r") as file:
 content=file.read()
 print(content)
