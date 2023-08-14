import matplotlib.pyplot as plt
def plot_monthly_data(months, temperatures, rainfall):
    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(months, temperatures, marker='o', linestyle='-')
    plt.xlabel('Month')
    plt.ylabel('Temperature (Celsius)')
    plt.title('Monthly Temperature Data')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.scatter(months, rainfall)
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.title('Monthly Rainfall Data')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    temperatures = [25, 27, 28, 30, 32, 35, 36, 37, 38, 39, 28, 36]
    rainfall = [40, 55, 80, 75, 100, 115, 130, 70, 85, 45, 30, 105]
    plot_monthly_data(months, temperatures, rainfall)
