def get_data():
    with open ('name.txt') as f:
        content = f.read()
        content = content.split()
        return content