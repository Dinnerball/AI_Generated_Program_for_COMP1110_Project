def longest_increasing_run(numbers):
    if not numbers:
        return []
    
    max_run = []
    current_run = [numbers[0]]
    
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            current_run.append(numbers[i])
        else:
            if len(current_run) > len(max_run):
                max_run = current_run
            current_run = [numbers[i]]
            
    if len(current_run) > len(max_run):
        max_run = current_run
        
    return max_run

