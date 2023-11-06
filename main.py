import argparse

vaild_chars = ["0", "1", "2", "3", "4", "|", " "]
easyimagecli = argparse.ArgumentParser("EasyImage")
easyimagecli.add_argument("file", type=str, help="The file to read.")
args = easyimagecli.parse_args()
file = args.file

# The InvalidColor class is an exception class that can be raised when an invalid color is
# encountered.


class InvaildColor(Exception):
    """The InvalidColor class is an exception class that can be raised when an invalid color is
    encountered."""

    def __init__(self, color: str, line: int):
        if type(color) != "int":
            print("Invaild color: {0}\nLine: {1}".format(color, line))
        else:
            print('Invaild color: "{0}"\nLine: {1}'.format(color, line))

        exit()


# The InvalidPath class is an exception that can be raised when an invalid file path is encountered.
class InvaildPath(Exception):
    """The InvalidPath class is an exception that can be raised when an invalid file path is encountered."""

    def __init__(self, path: str):
        print('Error: Invaild Path\nPath is: {0}'.format(path))
        exit()


def read(filename: str):
    """
    The `read` function reads a file, replaces certain characters with corresponding colors, and returns
    a list of colors.

    Args:
      filename (str): The `filename` parameter is a string that represents the name of the file that you
    want to read. It should include the file extension (e.g., "example.ei").

    Returns:
      a list of colors, where each color is represented by a string.
    """
    """
    The function reads a file, replaces certain characters with corresponding colors, and returns a list
    of colors.

    :param filename: The `filename` parameter is a string that represents the name of the file that you
    want to read. It should include the file extension (e.g., "example.ei")
    :type filename: str
    :return: a list of colors, where each color is represented by a string.
    """
    """
    The function reads a file, replaces certain characters with corresponding colors, and returns a list
    of colors.
    
    :param filename: The parameter `filename` is a string that represents the name of the file that you
    want to read
    :return: a list of colors, where each color is represented by a string.
    """
    try:
        with open(filename, "r") as f:
            file = f.readlines()
    except FileNotFoundError:
        raise InvaildPath(filename)

    current_line = 1

    for line in file:
        colorslist = []
        line = list(line.replace(",", ""))
        for item in line:
            if item not in vaild_chars:
                raise InvaildColor(item, current_line)
            if item == "|":
                current_line += 1
            colorslist.append(
                item.replace("0", "black")
                .replace("1", "white")
                .replace("2", "red")
                .replace("3", "green")
                .replace("4", "blue")
            )
    return colorslist


def export(colors: list, path: str):
    """
    The function "export" takes a list of colors and a file path as input and does not perform any
    operations.

    Args:
      colors (list): The `colors` parameter is a list that contains the colors to be exported. It can be
    any list of colors, such as ["red", "blue", "green"] or ["#FF0000", "#0000FF", "#00FF00"].
      path (str): The `path` parameter is a string that represents the file path where the exported data
    will be saved. It should be a valid file path on the system where the code is running.
    """
    """
    The function "export" takes a list of colors and a file path as input and does not perform any
    operations.

    :param colors: The `colors` parameter is a list that contains the colors to be exported. It can be
    any list of colors, such as ["red", "blue", "green"] or ["#FF0000", "#0000FF", "#00FF00"]
    :type colors: list
    :param path: The `path` parameter is a string that represents the file path where the exported data
    will be saved
    :type path: str
    """
    """
    The function "export" takes a list of colors and a file path as input and does not perform any
    operations.

    :param colors: The `colors` parameter is a list that contains the colors to be exported
    :type colors: list
    :param path: The `path` parameter is a string that represents the file path where the exported data
    will be saved
    :type path: str
    """
    pass


print(read(file))
