import pandas as pd
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Downtown', 'Uptown', 'Suburb', 'Downtown', 'Uptown'],
    'number_of_bedrooms': [3, 5, 4, 6, 3],
    'area_in_sqft': [1200, 3000, 1800, 3500, 1600],
    'listing_price': [500000, 750000, 600000, 850000, 550000]
}
property_data = pd.DataFrame(data)
average_price_per_location = property_data.groupby('location')['listing_price'].mean()
properties_with_more_than_4_bedrooms = property_data[property_data['number_of_bedrooms'] > 4].shape[0]
property_with_largest_area = property_data.loc[property_data['area_in_sqft'].idxmax()]
print("Average listing price in each location:")
print(average_price_per_location)

print(f"\nNumber of properties with more than four bedrooms: {properties_with_more_than_4_bedrooms}")

print("\nProperty with the largest area:")
print(property_with_largest_area)
