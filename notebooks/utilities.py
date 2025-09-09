# Filter data
def filter_bits(bitmask, bits_to_check=[13, 14]):
    """
    Filter bitmask to check if bits are set.
    
    Parameters
    ----------
    bitmask : int
        Integer bitmask to check.
    bits_to_check : list of int, optional
        List of bit positions to check (0-indexed). Default is [13, 14].
    """
    flagged = []
    for bit in bits_to_check:
        flagged.append((bitmask & 2**bit) > 0)
    return not any(flagged)