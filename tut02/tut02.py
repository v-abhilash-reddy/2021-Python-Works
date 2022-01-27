def get_memory_score(input_nums):
    #checking for invalid numbers
    invalid_list = []
    for i in range(len(input_nums)):
        if(type(input_nums[i])!=int):
            invalid_list.append(input_nums[i])
    if(len(invalid_list)!=0):
        print("\nPlease enter a valid input list.")
        print("Invalid inputs detected : ",invalid_list)
        return -1
    ct = 0
    fibox = []
    for i in range(len(input_nums)):
        x = 0
        for j in range(len(fibox)):
            if input_nums[i]==fibox[j]: 
                ct += 1
                x = 1
                break
        if x==0:
            if len(fibox)==5:
                fibox.pop(0)
            fibox.append(input_nums[i])
    return ct
    
input_nums = [7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
k = get_memory_score(input_nums)
if(k!=-1):
    print("Score : ",k)