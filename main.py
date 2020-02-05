import random as rnd

### Implementation ###

def shared_tasks(X, Y, i, j, DP, R = []):
    if i == 0 or j == 0:
        return
    if X[i-1] == Y[j-1]:
        shared_tasks(X, Y, i-1, j-1, DP, R)
        R.append(X[i-1])
    elif DP[i-1][j] > DP[i][j-1]:
        shared_tasks(X, Y, i-1, j, DP, R)
    else:
        shared_tasks(X, Y, i, j-1, DP, R)
    return R

def sequenced_shared_tasks(X, Y):
    m = len(X)
    n = len(Y)
    # Create a DP solution table
    DP = [[0 for x in range(n+1)] for x in range(m+1)] 
  
    # Following steps build a DP[m+1][n+1] table in bottom up fashion.
    # DP[i][j] contains length of largest sequenced common tasks  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                DP[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                DP[i][j] = DP[i-1][j-1] + 1
            else: 
                DP[i][j] = max(DP[i-1][j], DP[i][j-1]) 
  
    # Following code is used to find largest sequenced common tasks
    # Start from the right-most and bottom-most corner of DP table and 
    # store each sequenced common task into sequenced tasks list of R
    return shared_tasks(X, Y, m, n, DP, [])

### Test Cases ###

print("Test Case 1")

P = ['V','Y','X','Y','U','V','W','W']
Q = ['Y','V','X','U','U','V']

print("Tasks Bag P\t\t: ",P)
print("Tasks Bag Q\t\t: ",Q)

R = sequenced_shared_tasks(P, Q)
print("Seq. Shared Tasks Bag R\t: ",R)

print("Test Case 2")

L_MIN = 5
L_MAX = 10

T = 'UVWXY'
P = [rnd.choice(T) for i in range(rnd.randint(L_MIN, L_MAX))]
Q = [rnd.choice(T) for i in range(rnd.randint(L_MIN, L_MAX))]

print("Tasks Bag P\t\t: ",P)
print("Tasks Bag Q\t\t: ",Q)
R = sequenced_shared_tasks(P, Q)
print("Seq. Shared Tasks Bag R\t: ",R)

print("Test Case 3")

L_MIN = 5
L_MAX = 10

T = 'UVWXY'
P = [rnd.choice(T) for i in range(rnd.randint(L_MIN, L_MAX))]
Q = [rnd.choice(T) for i in range(rnd.randint(L_MIN, L_MAX))]

print("Tasks Bag P\t\t: ",P)
print("Tasks Bag Q\t\t: ",Q)
R = sequenced_shared_tasks(P,Q)
print("Seq. Shared Tasks Bag R\t: ",R)

print("Test Case 4")

L_MIN = 5
L_MAX = 10

T = 'MNTUVXYZ'
P = [rnd.choice(T) for i in range(rnd.randint(L_MIN, L_MAX))]
Q = [rnd.choice(T) for i in range(rnd.randint(L_MIN, L_MAX))]

print("Tasks Bag P\t\t: ",P)
print("Tasks Bag Q\t\t: ",Q)
R = sequenced_shared_tasks(P, Q)
print("Seq. Shared Tasks Bag R\t: ",R)
