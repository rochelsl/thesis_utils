import math

def uncertainty_notation(val, err):
    """
    Format value and uncertainty as:
        value(error)

    Example:
        12.3456 ± 0.078  ->  12.35(8)
        1.234 ± 0.010    ->  1.234(10)
    """
    u = abs(err)
    # No uncertainty
    if u == 0:
        return str(val)
    # Determine initial decimal places
    if u >= 1:
        d = 0
    else:
        d = math.ceil(-math.log10(u))
    # Scale uncertainty and remove trailing zeros
    scaled_u = round(u * (10 ** d))
    while d > 0 and scaled_u % 10 == 0:
        d -= 1
        scaled_u = round(u * (10 ** d))
    # Round value to matching decimals
    rounded_val = round(val, d)
    # Format value
    if d > 0:
        value_str = f"{rounded_val:.{d}f}"
    else:
        value_str = f"{rounded_val:.0f}"
    return f"{value_str}({scaled_u})"
    
if __name__ == "__main__":
    test_val, test_err = 45267.73589, 0.092
    print(uncertainty_notation(test_val, test_err))