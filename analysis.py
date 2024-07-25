import pandas as pd

def run_analysis():
    # Load data
    data = pd.read_csv('data/sales_data.csv')
    
    # Perform analysis (e.g., calculate total sales and mean sales per product)
    total_sales = data['sales'].sum()
    mean_sales_per_product = data.groupby('product')['sales'].mean().to_dict()

    return {'total_sales': total_sales, 'mean_sales_per_product': mean_sales_per_product}
