def simplify_fraction(numerator, denominator):
    factor = greatest_common_factor(numerator, denominator)
    return (numerator // factor, denominator // factor)


def greatest_common_factor(x, y):
    """Return the greatest common factor between x and y."""
    x_factors = compute_factors(x)
    y_factors = compute_factors(y)
    common_factors = set(x_factors) & set(y_factors)
    if len(common_factors) > 0:
        return max(common_factors)
    else:
        return 1


def compute_factors(n):
    """Return all factors for a given n."""
    return [i for i in range(1, n + 1) if n % i == 0]
