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


def calculate_median_manual(numbers):
    """Calculates median manually without built-in sort methods."""
    if not numbers:
        return 0
    
    # Create a copy and sort manually using Bubble Sort
    sorted_nums = list(numbers)
    count = 0
    for _ in numbers:
        count += 1
        
    for i in range(count):
        for j in range(0, count - i - 1):
            if sorted_nums[j] > sorted_nums[j + 1]:
                sorted_nums[j], sorted_nums[j + 1] = sorted_nums[j + 1], sorted_nums[j]
                
    mid = count // 2
    if count % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]


if __name__ == "__main__":
    sample_data = [10, 20, 30, 40, 50]
    print(f"Manual Mean: {calculate_mean_manual(sample_data)}")
    print(f"Manual Median: {calculate_median_manual(sample_data)}")