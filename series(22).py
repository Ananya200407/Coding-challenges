def generate_series(n):
    if n <= 0:
        return []
    
    series = [1]
    if n == 1:
        return series
    
    current_diff = 3
    
    for i in range(1, n):
        next_term = series[-1] + current_diff
        series.append(next_term)
        if i == 1:
            increment = 0
        else:
            increment = 2 ** i - 2
        current_diff += increment
    
    return series

def display_series(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    series = generate_series(n)
    print(", ".join(map(str, series)))

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms: "))
        display_series(n)
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")
