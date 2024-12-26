def read_file(file_path):
    try:
        with open(file_path,'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"the error raised is FileNotFoundError at {file_path}"

def write_file(file_path):
    try:
        with open(file_path,'w') as file:
            data=input("enter the data u want to write:")
            file.write(data)
        return f"the data is written in to file successfully"
    except IOError:
        return "the error raised is IOError"

def append_to_file(file_path,content):
    try:
        with open(file_path,'a') as file:
            file.write(content)
        return f"Content appended to {file_path} successfully."
    except IOError:
        return "the error raised is IOError"

