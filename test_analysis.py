from data-analytics-app.src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()
    assert 'total_sales' in results
    assert 'mean_sales_per_product' in results
    assert results['total_sales'] > 0
