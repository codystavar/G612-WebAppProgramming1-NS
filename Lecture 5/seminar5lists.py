# lists
list = []

n = input()
n = int(n)

for i in range(n):
    line = input()
    line_elements = line.split(" ")
    cho = line_elements[0]
    if cho == "insert":
        i = line_elements[1]
        i = int(i)
        e = line_elements[2]
        e = int(e)
        list.insert(i, e)
    else:
        if cho == "print":
            print(list)
        else:
            if cho == "remove":
                e = line_elements[1]
                e = int(e)
                list.remove(e)
            else:
                if cho == "append":
                    e = line_elements[1]
                    e = int(e)
                    list.append(e)
                else:
                    if cho == "sort":
                        list.sort()
                    else:
                        if cho == "pop":
                            list.pop()
                        else:
                            if cho == "reverse":
                                list.reverse()
                            else:
                                print("Invalid command(s)")
