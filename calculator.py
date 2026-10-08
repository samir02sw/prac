def calculate_mean_manual(numbers):
    """Calculates mean manually without sum() or len() built-ins."""
    if not numbers:
        return 0

    total_sum = 0
    count = 0

    for num in numbers:
        total_sum += num
        count += 1

    return total_sum / count

if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    print(f"Manual Mean: {calculate_mean_manual(sample_data)}")