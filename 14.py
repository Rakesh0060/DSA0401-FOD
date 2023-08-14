import pandas as pd

def calculate_age_frequency_distribution(df):
    age_freq = df[df['Purchase']]['Age'].value_counts().sort_index()
    return age_freq

def main():
    n = int(input("Enter the number of customers: "))
    
    data = []
    for i in range(n):
        customer_id = i + 1
        age = int(input(f"Enter the age of customer {customer_id}: "))
        purchase = input(f"Did customer {customer_id} make a purchase (yes/no)? ").lower() == 'yes'
        data.append((customer_id, age, purchase))

    df = pd.DataFrame(data, columns=['Customer_ID', 'Age', 'Purchase'])
    age_distribution = calculate_age_frequency_distribution(df)

    print("\nFrequency Distribution of Customer Ages:")
    for age, freq in age_distribution.items():
        print(f"{age}: {freq}")

if __name__ == "__main__":
    main()
