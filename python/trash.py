import functools

@functools.lru_cache(maxsize=None)
def expensive_calculation(n):
    # Some expensive calculation here
    return n * 2

# Example usage:
print(expensive_calculation(5))  # Output: 10
print(expensive_calculation(5))  # Output: 10 (cached result)

# Clear the cache:
expensive_calculation.cache_clear()

print(expensive_calculation(5))  # Output: 10 (since the cache was cleared, it recomputes the result)
