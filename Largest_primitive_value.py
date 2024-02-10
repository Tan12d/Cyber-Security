p=13

def primitive_check(i,p):
    list=[]
    print(f'Main {i}')
    for j in range(1,p):
        rem= pow(i,j)%p
        list.append(rem)
        
    list.sort()
    print(list)
    
    for k in range(1,p):
        if k!=list[k-1]:
            return False
            
    return True
        
        
def pri(p):
    for i in range(p-1,0,-1):
        if primitive_check(i,p):
            return i
            
print(f'alpha= {pri(p)}')