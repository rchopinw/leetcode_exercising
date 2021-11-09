# LC 477: Calculating the total hamming distance
def hamming_distances(nums):
    return sum(x.count('1') * x.count('0') for x in zip(*map('{:032b}'.format, nums)))

