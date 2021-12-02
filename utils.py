def read_file(filename):
    with open(filename, "r") as data:
        return data.read().splitlines()
