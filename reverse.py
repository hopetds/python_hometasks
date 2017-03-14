def reverse(n):
    """Returns n with all digits reversed. Assume positive n."""
    #your code here
    number=n
    rev = 0
    while n > 0:
        rev=(10*rev) + n%10
        n //=10
    #while number:
    #    digit = number % 10
    #    number //=10
    print rev
reverse(110201)
