def solution(A):
    distinct_products = set()
    product = 1
    
    for num in A:
        product *= num
    
    for num in A:
        distinct_products.add(product// num)
        
    return len(distinct_products)
    
print(solution([9, 16, 4]))  
print(solution([3, 4, 2, 3, 1])) 
print(solution([10000000000, 10000000000]))
