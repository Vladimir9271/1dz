def fib (num):
    if num == 0 or num == 1:
        return num
    else:
        return fib(num -1) + fib(num - 2)
arr=[]
def primenumber (num ):
    pr = True
    for b in range(2,num):
         if num % b == 0 :
                pr = False
    if pr and num != 1:
        arr.append(num % 10)
with open("in_nums.txt","r",) as file:
    for row in file:
        primenumber(int(row.strip()))
    file.close()

print(arr)

with open("out_nums.txt","w",) as file:
    for row in arr:
        file.write(str(fib(row))+"\n")
    file.close()