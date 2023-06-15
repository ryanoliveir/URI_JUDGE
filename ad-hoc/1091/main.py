

while True:
    
    K = int(input())
    if(K == 0):
        break
    
    N, M = input().split(' ')
    N, M = int(N), int(M)
    
    count = 0
    
    while count < K:
        X, Y = input().split(' ')

        X, Y = int(X), int(Y)
        
        if(X == N or Y== M):
            print("divisa")
        
        if(X < N and Y > M):
            print("NO")
        
        if(X > N and Y > M):
            print("NE")
        
        if(X > N and Y < M):
            print("SE")
        
        if(X < N and Y < M):
            print("SO")
            
        count+= 1




