#meraki function 
def callmeraki(t):
    r1 = t%10
    t = t//10
    while(t):
        r2 = t%10
        if(abs(r1-r2)!=1):
            return 0
        r1 = r2
        t = t//10    
    return 1

ct = 0 #ct variable used to count meraki numbers
#input : list of positive numbers are given below
no_list = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321]

for i in range(len(no_list)) :
    if(callmeraki(no_list[i])):
        ct += 1
        print("Yes - ",no_list[i]," is a Meraki number")
    else : print("No - ",no_list[i]," is NOT a Meraki number")

print("\nThe input list contains :")
print(ct,"  Meraki numbers\n",len(no_list)-ct," Non Meraki numbers\n")