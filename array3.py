#1
import array
arr=array.array('i', [10, 20, 30, 40, 50])
print(arr[0])
print(arr[2])
print(arr[4])

#2
import array
arr = array.array('i', [10, 20, 30, 40, 50])

print(arr[-1])  
print(arr[-2])  
print(arr[-5]) 

#3 
import array
arr = array.array('i', [10, 20, 30, 40, 50])
arr[2] = 35
print(arr)