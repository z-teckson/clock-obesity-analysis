#!/usr/bin/env python3
"""
Preprocessing script for CLOCK gene obesity analysis.
Includes MAF filtering for genetic variants.
"""

import pandas as pd

def filter_by_maf(data, maf_threshold=0.01):
    """
    Filter variants by Minor Allele Frequency.
    
    Args:
        data: DataFrame with 'MAF' column
        maf_threshold: variants with MAF below this threshold are removed
        
    Returns:
        Filtered DataFrame
    """
    filtered = data[data['MAF'] >= maf_threshold]
    print(f"Removed {len(data) - len(filtered)} variants with MAF < {maf_threshold}")
    return filtered

if __name__ == "__main__":
    # Load data
    df = pd.read_csv("data/variants.csv")
    # Apply MAF filter
    df_filtered = filter_by_maf(df)
    df_filtered.to_csv("data/filtered_variants.csv", index=False)