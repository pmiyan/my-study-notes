#given a number, return it's reverse

def reverse_num(num):
    reverse = 0
    while(num>0):
        reverse = (reverse*10) + int(num%10)
        num = int(num/10)
    print(reverse)
    return reverse

num_lst = [1234, 1001, 100]
for num in num_lst:
    print(reverse_num(num))


sub = "full"
str1 = "Awful"
print(str1.find(sub))