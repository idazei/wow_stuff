import curses


binary_chart = [128, 64, 32, 16, 8, 4, 2, 1]

octet = input("Please put in octet?\n")

int_octet_list = []
octet_list = []
total = 0

# puts input in a list
for i in octet:
    octet_list += i

# checks if input is a octet if not it breaks.
if len_octet != 8:
    print("Not a octet")
    quit

# checks for 1 or 0 then changes number to chart number.
for i in octet_list:
    if i == "0":
        continue
    if i == "1":
        if i == octet_list[0]:
            octet_list[0] = binary_chart[0]
        elif i == octet_list[1]:
            octet_list[1] = binary_chart[1]
        elif i == octet_list[2]:
            octet_list[2] = binary_chart[2]
        elif i == octet_list[3]:
            octet_list[3] = binary_chart[3]
        elif i == octet_list[4]:
            octet_list[4] = binary_chart[4]
        elif i == octet_list[5]:
            octet_list[5] = binary_chart[5]
        elif i == octet_list[6]:
            octet_list[6] = binary_chart[6]
        elif i == octet_list[7]:
            octet_list[6] = binary_chart[6]

# changes to int and adds up.
for i in octet_list:
    int_octet_list.append(int(i))
for i in int_octet_list:
    total += i

print(total)