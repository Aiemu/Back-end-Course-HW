import csv
import sys

def quick_sort(list, left, right, loc):
    if left >= right:
        return

    par = list[left][loc]
    l = left
    l_plus = left + 1
    r_plus = right + 1

    while l_plus < r_plus:
        if list[l_plus][loc] < par:
            list[l_plus], list[l + 1] = list[l + 1], list[l_plus]
            l += 1
            l_plus += 1
        elif list[l_plus][loc] == par:
            l_plus += 1
        else:
            list[l_plus], list[r_plus - 1] = list[r_plus - 1], list[l_plus]
            r_plus -= 1
    list[left], list[l] = list[l], list[left]

    quick_sort(list, left, l - 1, loc)
    quick_sort(list, r_plus, right, loc)

def analyse():
    DESC = False
    cmd_list = sys.argv

    print(cmd_list)
    input_path = cmd_list[1]
    output_path = cmd_list[len(cmd_list) - 1]
    name = cmd_list[2]
    data = []

    if len(cmd_list) == 4:
        pass
    elif len(cmd_list) == 5 and cmd_list[3] == "DESC": 
        DESC = True
    else: 
        print("Error: Wrong command format!")
        return
    
    try:
        with open(input_path, "r") as fi:
            csv_data = fi.read()
            csv_data = csv_data.split("\n")

            for row in csv_data:
                List = []
                List = row.split(",")
                data.append(List)

            loc = data[0].index(name)

            if loc == -1:
                print("Error: Key word not exist!")
                return

            for row in range(len(data) - 1, 0, -1):
                # 倒序遍历
                try:
                    float(data[row][loc])
                except:
                    del data[row]
            print 
            quick_sort(data, 1, len(data) - 1, loc)

    except IOError:
        print("Error: Input file not exist!")
        return

    try:
        with open(output_path, "w") as fo:
            tmp = ",".join(data[0])
            fo.write(tmp + "\n")
            if DESC:
                for row in range(len(data) - 1, 0, -1):    
                    tmp = ",".join(data[row])
                    fo.write(tmp + "\n")
            else:
                for row in range(1, len(data)):    
                    tmp = ",".join(data[row])
                    fo.write(tmp + "\n")

    except IOError:
        print("Error: Output file creat failed!")
        return

    # print(data)

    fi.close()
    fo.close()

# input.txt C1 DESC output-csv.txt
# input.txt 3 output-csv.txt

if __name__=="__main__":
    analyse()
