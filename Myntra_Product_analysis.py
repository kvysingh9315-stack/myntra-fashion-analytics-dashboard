import pandas as pd
df = pd.read_csv('Myntra_Clothing.csv.zip')
df.drop(columns=['URL', 'Description'], inplace=True)


df['DiscountPrice (in Rs)'].fillna(df['DiscountPrice (in Rs)'].mean(), inplace=True)
df['DiscountOffer'].fillna(df['DiscountOffer'].mode()[0], inplace=True)
df['Ratings'].fillna(0.00, inplace=True)
df['Reviews'].fillna(0, inplace=True)

df.drop_duplicates(inplace=True)
print(df.info())
print(df.describe())

Total_Brands = df['BrandName'].value_counts()
print('Top 10 Brands by Product Count:')
print(Total_Brands.head(10))

Categories=df['Category'].value_counts()
print('All categories of clothing and count of products in each category:')
print(Categories)

Highest_rated_products=df[df['Ratings']==df['Ratings'].max()]
print('top 10 highest rated products :',Highest_rated_products.head(10))

Lowest_rated_products=df[df['Ratings']==df['Ratings'].min()]
print('Top 10 lowest rated products :',Lowest_rated_products.head(10))

costliest_product=df[df['OriginalPrice (in Rs)']==df['OriginalPrice (in Rs)'].max()]
Cheapest_product=df[df['OriginalPrice (in Rs)']==df['OriginalPrice (in Rs)'].min()]
print('Costliest Product :',costliest_product)
print('Cheapest Product :',Cheapest_product)

top_rated_brands = df.groupby('BrandName')['Ratings'].mean().sort_values(ascending=False)
print('\nTop 5 Brands by Average Rating:')
print(top_rated_brands.head(5))

Most_reviewed_brand=df.groupby('BrandName')['Reviews'].sum().sort_values(ascending=False)
print('Top 5 most reviewed brands : ',Most_reviewed_brand.head(5))

avg_rating_category = df.groupby('Category')['Ratings'].mean().sort_values(ascending=False)
print('Average Rating per Category:')
print(avg_rating_category)

price_comparison = df.groupby('Category')[['OriginalPrice (in Rs)', 'DiscountPrice (in Rs)']].mean()
print('Avg Original vs Discount Price by Category:')
print(price_comparison)


df.to_csv('Myntra_cleaned.csv', index=False)
print('Clean data exported successfully!')