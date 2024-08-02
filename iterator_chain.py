import itertools

sales_region_1 = [100, 200, 300]
sales_region_2 = [400, 500, 600]
sales_region_3 = [700, 800, 900]

all_sales = itertools.chain(sales_region_1, sales_region_2, sales_region_3)

# Process combined data
for sale in all_sales:
    print(f"Processed sale amount: {sale}")
