#use all() and any() with conditions

num = [1,4,6,8,9]

if __name__ == "__main__":
    print("All Even Numbers? : ",all(n%2==0 for n in num)) #False
    print("Any Odd Numbers? : ",any(n%2==1 for n in num))  #True
    
    
"""সবগুলো True হলে True
all([True, True, True])    # True
all([True, False, True])   # False
all([False, False, False]) # False

# কোনোটি True হলে True  
any([False, False, True])  # True
any([False, False, False]) # False
any([True, True, True])"""   # True
