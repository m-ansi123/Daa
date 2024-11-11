def fibonacci_recursive(n):
	if n<=0:
		return []
	elif n ==1:
		return [0]
	elif n ==2:
		return [0,1]
	else:
		seq=fibonacci_recursive(n-1)
		seq.append(seq[-1]+seq[-2])
		return seq
n=int(input("Enter the n terms:"))
result=fibonacci_recursive(n)
print(f"Fibonacci sequence (first {n} terms):{result}")
     


def fibonacci_iterative(n):
    sequence =[]
    a,b =0,1
    for i in range(n):
        sequence.append(a)
        a,b=b,a+b
    return sequence
n=int(input("Enter the terms:"))
result=fibonacci_iterative(n)
print(f"fibonacci sequence (first{n}terms):{result}")


