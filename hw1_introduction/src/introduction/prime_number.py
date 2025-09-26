def is_prime_number(n):
    """Returns True if n is a prime number. Otherwise, returns False."""
    # 1.2 begin
    try:
        n = int(n)
    except (TypeError, ValueError):
        return False
    # 1.2 end
    
    # BEGIN QUESTION 1.1
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(n, "  F")
            return False
    print(n, "  T")
    return True
    # END QUESTION 1.1
