total_land = 80
segments = 5
land_per_crop = total_land / segments  

tomato_30 = 0.30 * land_per_crop * 10 * 1000 * 7
tomato_70 = 0.70 * land_per_crop * 12 * 1000 * 7
tomato_sales = tomato_30 + tomato_70

potato_sales = land_per_crop * 10 * 1000 * 20

cabbage_sales = land_per_crop * 14 * 1000 * 24

sunflower_sales = land_per_crop * 0.7 * 1000 * 200

sugarcane_sales = land_per_crop * 45 * 4000

total_sales = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales +
    sugarcane_sales
)

chemical_free_sales = (
    tomato_sales +
    potato_sales +
    cabbage_sales +
    sunflower_sales
)

print("Overall Sales from 80 acres: Rs.", total_sales)
print("Chemical-free Sales after 11 months: Rs.", chemical_free_sales)
