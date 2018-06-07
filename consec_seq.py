def rep_consec(list1,n):
 mm1=0  #mismatch1
 nextt=list1[n-1]-n+1  #calculating the next element
 for i in range(0,n-1): #starting case check with the miniimum element of the array
  if(nextt not in list1):  
   ans=list1[0]
   mm1+=1
  nextt+=1
 if(mm1==1): #if just one element is missing, directly print it
  return ans
 elif(mm1==0): #if any of the numbers are not missing, then the sequence is already consecutive
  return 0
 else: #if more than 2 elements are missing, go to max element check
  mm2=0
  nextt=list1[0]+n-1  
  for j in range(n-1,0,-1):  #starting case check with the maximum element of the array
   if(nextt not in list1):
    ans=list1[n-1]
    mm2+=1
   nextt-=1
  if(mm2==1): #only if one number is missing
   return ans
  else:    #if more than 2 elements are missing then, return -1 to say that consecutive sequence does not exist
   return -1

list1=[]
ele=raw_input("Replacing one element that makes array elements consecutive... \nEnter elements : ").split(" ")
for i in ele:
    j=int(i)  #converting the string to integer
    list1.append(j)    
list1.sort()   #sort
n=len(list1)/1  #finding the length of the list
final=rep_consec(list1,n) #calling the function to find the solution
if(final==0):
    print("Sequence is already consecutive")
elif(final==-1):
    print("Sequence cannot be made consecutive")
else:
    print "Ans : ",final
    
    
'''
Sample Input :
1 2 3 4 5
Sample Output :
Sequence is already consecutive
Explanation:
All the numbers are continous


Sample Input :
10 2 3 24 5
Sample Output :
Sequence cannot be made consecutive
Explanation:
There is no choice available where one of the numbers can be replaced in such a way that sequence becomes consecutive


Sample Input :
10 2 3 4 5
Sample Output :
10
Explanation:
the number 10 can be replaced with 1 or 6. That way, the sequence becomes continous. 
'''
