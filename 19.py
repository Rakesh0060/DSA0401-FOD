import numpy as np
from scipy import stats

def input_data(prompt, num_entries):
    data = []
    for _ in range(num_entries):
        entry = int(input(prompt))
        data.append(entry)
    return data

def calculate_confidence_interval(data):
    confidence_level = 0.95
    mean, std_dev = np.mean(data), np.std(data, ddof=1)
    sample_size = len(data)
    margin_of_error = stats.t.ppf((1 + confidence_level) / 2, df=sample_size - 1) * std_dev / np.sqrt(sample_size)
    return mean - margin_of_error, mean + margin_of_error

if __name__ == "__main__":
    new_drug_data = input_data("Enter the drug data:", int(input("Enter the no. of new drugs: ")))
    print(new_drug_data)
    
    placebo_data = input_data("Enter the placebo data:", int(input("Enter the no. of new placebos: ")))
    print(placebo_data)
    
    new_drug_lower, new_drug_upper = calculate_confidence_interval(new_drug_data)
    print(f"95% Confidence Interval for mean reduction in blood pressure (New Drug Group): [{new_drug_lower:.2f}, {new_drug_upper:.2f}]")

    placebo_lower, placebo_upper = calculate_confidence_interval(placebo_data)
    print(f"95% Confidence Interval for mean reduction in blood pressure (Placebo Group): [{placebo_lower:.2f}, {placebo_upper:.2f}]")
