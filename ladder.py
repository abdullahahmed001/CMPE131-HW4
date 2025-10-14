def my_steps(n):
    if n < 1 or n > 25:
        raise ValueError(f"Input {n} must be between 1 and 25")

    def climb(n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        return climb(n - 1) + climb(n - 2)
    return climb(n)


