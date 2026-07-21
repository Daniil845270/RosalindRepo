k, m, n = int(input()), int(input()), int(input())

s = k + m + n

kFirst = k/s * ((k+m+n-1)/(s-1))
mFirst = m/s * ((k+0.75*(m-1)+0.5*n)/(s-1))
nFirst = n/s * ((k+0.5*m)/(s-1))

result = kFirst + mFirst + nFirst

print(result)

