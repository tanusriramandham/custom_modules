def is_prime(n):
    if n<=1:
        return f"No it is not a prime number {False}"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return f"no it is not a prime number {False}"
        else:
            return f"Yes it is prime number {True}"