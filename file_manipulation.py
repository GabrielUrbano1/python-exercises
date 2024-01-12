

def read_file():
# this will open and read file content
    with open("read_file.txt", "r") as file:
        content = file.read()
        print("file content")
        print(content)

read_file()

# this will write content to the file
content_to_add = "some jibberish to be added to the file!"

with open("read_file.txt", "w") as file:
    # read_file()
    file.write("\n" + content_to_add)



# with open("read_file.txt", "r") as file:
#     content = file.read()
#     print("updated content")
#     print(content)