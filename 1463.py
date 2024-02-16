dynamic_list = [int(input())]
count = -1
flag = True
while(flag):
    length = len(dynamic_list)
    for i in range(length):
        if dynamic_list[i] % 3 == 0:
            dynamic_list.append(dynamic_list[i]//3)
        if dynamic_list[i] % 2 == 0:
            dynamic_list.append(dynamic_list[i]//2)
        dynamic_list.append(dynamic_list[i]-1) 
        
        if dynamic_list[i] == 1:
            flag = False
    dynamic_list = dynamic_list[length:]
    count += 1

print(count)
