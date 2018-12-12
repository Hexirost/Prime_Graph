#Convert from decimal to another base
EXTRA_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def convert(num, base):
    EXTRA_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    remainder = int(num)
    new_num = ""

    multiple = 1
    while remainder - pow(base,multiple) >= 0:
        multiple+=1

    for mul in range(multiple-1,-1,-1):
        power = pow(base, mul)
        factor = power
        inc = 0
        while factor < remainder+1:
            factor += power
            inc+=1
        if inc:
            remainder = remainder - factor + power
        digit = EXTRA_CHARS[inc]
        new_num+=digit
        #print("Debugging: ", power, factor, inc, remainder, digit)
    return new_num

def base_converter(file, base):
    fp = open(file, "r")

    with open(file) as fp:
        line = "True"
        base_file = open(file[:-4] + "_100000000_base_" + str(base) + ".txt","w+")

        while (line):
            line = fp.readline()
            if line:
                converted_num = convert(line, base)
                base_file.write(converted_num+"\n")

    base_file.close()

for base in range(20,20):
    base_converter("prime.txt", base)