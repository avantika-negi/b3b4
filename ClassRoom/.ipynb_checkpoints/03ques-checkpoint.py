# Write a function to count n and evaluate a= n* 10 for all values from 0 to n
import time
def count(n):
    for i in range(0,n):
        a=n*10
ns=[1000000,234234,34345,345,344,345]        
n=1000000

def wrapper(func,n):
#code to evaluate run time of function call count(n)       
    start_time= time.time()*1000000
#print(start_time)
    func(n)
    count(1000000) #timing this function call/execution
    end_time = time.time()*1000000
#print(end_time)

    print(f"\nTime to excute is {end_time - start_time}micro second")
    
for n in ns :
    wrapper(count,n)
    
    