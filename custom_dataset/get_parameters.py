
def get_parameters(file):
    with open(file, "r") as f:
        list_of_parameter_lists = []
        data = f.readlines()
        for line in data:
            list_of_parameter_lists.append(line.strip("\n").split(" "))
    return list_of_parameter_lists