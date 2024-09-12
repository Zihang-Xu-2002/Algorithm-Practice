# https://www.fastprep.io/problems/tiktok-max-shared-categories
from typing import List

# Implementing GCD function using the Euclidean algorithm
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def maxSharedCategories(favoriteCategories: List[int]) -> int:
    max_gcd = 0
    n = len(favoriteCategories)
    
    # Compare every pair to find the maximum GCD
    for i in range(n):
        for j in range(i + 1, n):
            max_gcd = max(max_gcd, gcd(favoriteCategories[i], favoriteCategories[j]))
    
    return max_gcd

favoriteCategories = [[4, 2, 6, 8],[3, 2, 5],[4, 8, 2, 16],[1, 2, 3, 4, 8, 9]]
for item in favoriteCategories:
    print(maxSharedCategories(item)) 