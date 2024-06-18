m=int(input())
n=input()

for i in range(m):
    print("*"*n)


n=int(input())
for i in range(n+1):
    print("*"*i)
    
    
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
    

print("1×1=1")
print("1×2=2 2×2=4")
print("1×3=3 2×3=6 3×3=9")
print("1×4=4 2×4=8 3×4=12 4×4=16")
print("1×5=5 2×5=10 3×5=15 4×5=20 5×5=25")
print("1×6=6 2×6=12 3×6=18 4×6=24 5×6=30 6×6=36")
print("1×7=7 2×7=14 3×7=21 4×7=28 5×7=35 6×7=42 7×7=49")
print("1×8=8 2×8=16 3×8=24 4×8=32 5×8=40 6×8=48 7×8=56 8×8=64")
print("1×9=9 2×9=18 3×9=27 4×9=36 5×9=45 6×9=54 7×9=63 8×9=72 9×9=81")


for i in range(1,10):
    for m in range(1,i+1):
        print("{0}*{1}={2:2d}".format(i,m,i*m),end=" ")
    print(" ")
    


n=int(input())
square=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if j==0:
            square[i][j]=1
        else:
            square[i][j]=square[i-1][j-1]+square[i-1][j]
        if square[i][j]!=0:
            if i==j:
                print(square[i][j])
            else:
                print(square[i][j],end=" ")