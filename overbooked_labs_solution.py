def solve():
    import sys
    input = sys.stdin.read().split('\n')
    ptr = 0
    T = int(input[ptr].strip())
    ptr += 1
    for case in range(1, T + 1):
        while ptr < len(input) and input[ptr].strip() == '':
            ptr += 1
        if ptr >= len(input):
            break
        S, C = map(int, input[ptr].strip().split())
        ptr += 1
        lab_counts = {}
        for _ in range(S):
            while ptr < len(input) and input[ptr].strip() == '':
                ptr += 1
            if ptr >= len(input):
                break
            parts = input[ptr].strip().split()
            if len(parts) < 3:
                ptr += 1
                continue
            lab, time, _ = parts[0], parts[1], parts[2]
            key = (lab, time)
            lab_counts[key] = lab_counts.get(key, 0) + 1
            ptr += 1
        overbooked = []
        for (lab, time), count in lab_counts.items():
            if count > C:
                overbooked.append((lab, time, count - C))
        print(f"Case #{case}:")
        if not overbooked:
            print("No overbooking detected")
        else:
            for lab, time, excess in sorted(overbooked):
                print(f"{lab} {time}: Overbooked by {excess} student(s)")

solve()
