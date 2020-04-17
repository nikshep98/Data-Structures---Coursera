# python3

import sys

s = sys.stdin.readline()
q = int(sys.stdin.readline())

def Rabin_Karp_Matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = pow(d,m-1,q)
    p = 0
    t = 0
    result = []
    for i in range(m):
        p = pow(d*p+ord(pattern[i]),1,q)
        t = pow(d*t+ord(text[i]),1,q)
    for s in range(n-m+1):
        if p == t:
            match = True
            for i in range(m):
                if pattern[i] != text[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < n-m:
            t = pow(t-h*ord(text[s]),1,q)
            t = pow(t*d+ord(text[s+m]),1,q)
            t = pow(t+q,1,q)
    return result
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	my_list = Rabin_Karp_Matcher(s[a:a+l],s[b:b+l],257,11)
	if len(my_list)!=0 and my_list[0]==0:
	    print("Yes")
	else:
	    print("No")
