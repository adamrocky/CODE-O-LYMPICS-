def digit_sum_cycle_count(N):
    original = N
    count = 0
    
    while True:
        # Handle single-digit numbers (e.g., 7 → 07)
        tens = N // 10 if N >= 10 else 0
        units = N % 10
        
        digit_sum = tens + units
        new_number = (units * 10) + (digit_sum % 10)
        count += 1
        
        if new_number == original:
            return count
        
        N = new_number

# Read input and print output
N = int(input())
print(digit_sum_cycle_count(N))
