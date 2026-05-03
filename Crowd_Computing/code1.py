def crowd_estimate(estimates):
    n = len(estimates)
    
    # Mean (average)
    mean_estimate = sum(estimates) / n
    
    # Median
    sorted_estimates = sorted(estimates)
    if n % 2 == 0:
        median_estimate = (sorted_estimates[n//2 - 1] + sorted_estimates[n//2]) / 2
    else:
        median_estimate = sorted_estimates[n//2]
    
    # Trimmed Mean (removes extreme outliers)
    trim_percent = 0.1  # remove top & bottom 10%
    k = int(n * trim_percent)
    trimmed = sorted_estimates[k:n-k] if n > 2*k else sorted_estimates
    trimmed_mean = sum(trimmed) / len(trimmed)
    
    return mean_estimate, median_estimate, trimmed_mean


# ---- Example Usage ----
if __name__ == "__main__":
    # Example crowd guesses
    estimates = [120, 150, 130, 140, 1000, 135, 145, 138, 142, 137]

    mean_val, median_val, trimmed_val = crowd_estimate(estimates)

    print("Crowd Estimates:", estimates)
    print(f"Mean Estimate: {mean_val}")
    print(f"Median Estimate: {median_val}")
    print(f"Trimmed Mean Estimate: {trimmed_val}")