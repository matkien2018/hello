def print_n(x):
    for i in range(1,x+1):
        print(i)

def sum_n(x):
    y = 0
    for i in range(1,x+1)  :
        y += i
    return y

def sum_n2(x):
    return (1+x)*x/2

def sum_them():
    ret = 0
    val = int(input("In put a number: "))
    out_put = "The sum of: "
    while val != -1 :
        ret = ret + val
        out_put = out_put + str(val) + " + "
        val = int(input("In put another number: "))

    return out_put[:-3] + " = " + str(ret)

def boot_it(some_str,i_start,i_end):
    out_put =""
    i = 0
    while i < len(some_str):
        if i < i_start or i > i_end:
            out_put = out_put + some_str[i]
            i += 1
        else:
            i +=1
    return out_put

def strip(some_str,left_right):
    ret_str = "'"

    if left_right == "left":
        i = 0
        while i < len(some_str):
            if some_str[i] == " ":
                i += 1
            else:
                while i < len(some_str):
                    ret_str = ret_str + some_str[i]
                    i += 1
                break

    if left_right == "right":
        i = 0
        stop = 1
        while stop < len(some_str):
            if some_str[-stop] == " ":
                stop += 1
            else:
                while i <= (len(some_str) - stop) :
                    ret_str = ret_str + some_str[i]
                    i += 1
                break    


    ret_str = ret_str + "'"
    return ret_str

def is_tar(some_str: str) -> bool:
    is_t: bool = False
    is_a: bool = False
    is_r: bool = False
    i:int = 2

    if len(some_str) < 3:
        return False

    if  some_str[0] == "t":
        is_t = True
    else:
        is_t = False

    if some_str[1] == "a":
        is_a = True
    else:
        is_a = False
    
    while i < len(some_str) - 1:
        if some_str[i] == "a":
            i += 1
        else:
            is_a = False
        break

    if some_str[-1] == "r":
        is_r = True

    if is_t and is_a and is_r:
        return True
    else:
        return False



#print_n(100)
#print(sum_n(100))
#print(sum_n2(100))
##print(sum_them())
#print(boot_it("0123456789",2,4))
#print(strip("    hello    ","left"))
print(strip("    hello    ","right"))

#print(is_tar("tatr"))