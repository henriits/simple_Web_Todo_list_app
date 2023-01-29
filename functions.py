FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Opens and reads the file in filepath,
    returns a list of todo items. """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """This function acts as procedure,
    writes new todos in the list to a text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    