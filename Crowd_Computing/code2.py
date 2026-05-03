import matplotlib.pyplot as plt

def crowd_estimate(estimates, actual):
    n = len(estimates)

    # Mean
    mean_est = sum(estimates) / n

    # Median
    sorted_est = sorted(estimates)
    if n % 2 == 0:
        median_est = (sorted_est[n//2 - 1] + sorted_est[n//2]) / 2
    else:
        median_est = sorted_est[n//2]

    # Trimmed Mean (10%)
    k = int(0.1 * n)
    trimmed = sorted_est[k:n-k] if n > 2*k else sorted_est
    trimmed_mean = sum(trimmed) / len(trimmed)

    # Error %
    def error(est):
        return abs(est - actual) / actual * 100

    return {
        "mean": (mean_est, error(mean_est)),
        "median": (median_est, error(median_est)),
        "trimmed_mean": (trimmed_mean, error(trimmed_mean))
    }


def plot_estimates(estimates, actual, results):
    plt.figure()

    # Plot histogram of crowd guesses
    plt.hist(estimates, bins=10)

    # Vertical lines
    plt.axvline(actual, linestyle='dashed', label="Actual Value")
    plt.axvline(results["mean"][0], linestyle='dashed', label="Mean")
    plt.axvline(results["median"][0], linestyle='dashed', label="Median")
    plt.axvline(results["trimmed_mean"][0], linestyle='dashed', label="Trimmed Mean")

    plt.title("Crowd Estimation Analysis")
    plt.xlabel("Estimates")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


# -------- MAIN PROGRAM --------
if __name__ == "__main__":
    n = int(input("Enter number of people: "))

    estimates = []
    for i in range(n):
        val = float(input(f"Enter estimate {i+1}: "))
        estimates.append(val)

    actual = float(input("Enter actual number of gems: "))

    results = crowd_estimate(estimates, actual)

    print("\n--- Results ---")
    for key, (value, err) in results.items():
        print(f"{key.capitalize()} Estimate: {value:.2f} | Error: {err:.2f}%")

    plot_estimates(estimates, actual, results)