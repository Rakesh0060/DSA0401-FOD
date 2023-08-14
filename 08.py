import pandas as pd
 
data = {
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product C'],
    'quantity_sold': [20, 50, 60, 80, 110, 60, 70]
}
sales_data = pd.DataFrame(data)
top_5_products = sales_data.groupby('product_name')['quantity_sold'].sum().sort_values(ascending=False).head(5)
print("Top 5 products sold the most in the past month:")
print(top_5_products)
