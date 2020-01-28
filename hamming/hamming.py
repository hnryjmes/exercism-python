def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Something")

    zipped = list(zip(list(strand_a), list(strand_b)))
    count = 0
    for a, b in zipped:
        if a != b:
            count += 1

    return count
