import os

def check_csv(file_list, path):
    error_list = []

    for file in file_list:
        print("file", file)
        check = open(path+'\\'+file, 'r')
        lines = check.readlines()
        if len(lines) != 1:
            error_list.append(file)
            print("lines", len(lines))
            continue
        fields = lines[0].split(",")
        if len(fields) != 6:
            error_list.append(file)
            print("size", len(fields))
            continue

        # testing the int fields
        print("first_e", type(fields[0])!=type(5))
        if fields[0].isnumeric()!=True:
            error_list.append(file)
            continue
        print("second_e", type(fields[0])!=type(5))
        if fields[1].isnumeric()!=True:
            error_list.append(file)
            continue

        # testing the strings fields
        if type(fields[2])!=type(""):
            error_list.append(file)
            continue
        if type(fields[3])!= type(""):
            error_list.append(file)
            continue
        if type(fields[4])!=type(""):
            error_list.append(file)
            continue
        if type(fields[5])!=type(""):
            error_list.append(file)
            continue

    return error_list

def find_csv(files):
    file_list = []
    for file in files:
        results = file.find(".csv")
        if results != -1:
            file_list.append(file)
    return file_list

def write_errors(list_errors):
    #we intentionally overwrite for every time the program is run
    f = open("csv_with_errors.txt", "w")
    f.writelines(list_errors)

if __name__ == '__main__':
    curr_dir = os.getcwd()
    path = curr_dir + "/csv_here"
    #path = curr_dir
    files = os.listdir(path)
    result = find_csv(files)
    print(result)
    wrong_files = check_csv(result, path)
    print(wrong_files)
    write_errors(wrong_files)


