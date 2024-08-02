import pandas as pd
import random
import os
from faker import Faker

DATA_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Data")
print("Your data is stored at: ", DATA_FOLDER)

fake = Faker()

# Number of entities
num_users = 10000
num_products = 5000
num_orders = 20000
num_categories = 1000
num_reviews = 15000

# Generate Users
users = []
for i in range(num_users):
    users.append({
        'user_id': i,
        'name': fake.name(),
        'email': fake.email()
    })

# Generate Products
products = []
for i in range(num_products):
    products.append({
        'product_id': i,
        'product_name': fake.word(),
        'price': round(random.uniform(10, 100), 2)
    })

# Generate Categories
categories = []
for i in range(num_categories):
    categories.append({
        'category_id': i,
        'category_name': fake.word()
    })

# Generate Orders
orders = []
for i in range(num_orders):
    orders.append({
        'order_id': i,
        'user_id': random.randint(0, num_users-1),
        'order_date': fake.date_time_this_year()
    })

# Generate Reviews
reviews = []
for i in range(num_reviews):
    reviews.append({
        'review_id': i,
        'product_id': random.randint(0, num_products-1),
        'user_id': random.randint(0, num_users-1),
        'review_text': fake.text(),
        'rating': random.randint(1, 5)
    })

# Generate Relationships (Edges)
user_buys_product = []
order_contains_product = []
product_belongs_to_category = []
user_writes_review = []

for i in range(num_orders):
    user_id = orders[i]['user_id']
    product_ids = random.sample(range(num_products), random.randint(1, 5))
    for product_id in product_ids:
        user_buys_product.append({
            'user_id': user_id,
            'product_id': product_id
        })
        order_contains_product.append({
            'order_id': i,
            'product_id': product_id
        })

for i in range(num_products):
    category_id = random.randint(0, num_categories-1)
    product_belongs_to_category.append({
        'product_id': i,
        'category_id': category_id
    })

for review in reviews:
    user_writes_review.append({
        'review_id': review['review_id'],
        'user_id': review['user_id']
    })

# Convert to DataFrames
df_users = pd.DataFrame(users)
df_products = pd.DataFrame(products)
df_categories = pd.DataFrame(categories)
df_orders = pd.DataFrame(orders)
df_reviews = pd.DataFrame(reviews)
df_user_buys_product = pd.DataFrame(user_buys_product)
df_order_contains_product = pd.DataFrame(order_contains_product)
df_product_belongs_to_category = pd.DataFrame(product_belongs_to_category)
df_user_writes_review = pd.DataFrame(user_writes_review)

# Save to CSV
df_users.to_csv(os.path.join(DATA_FOLDER, 'users.csv'), index=False)
df_products.to_csv(os.path.join(DATA_FOLDER, 'products.csv'), index=False)
df_categories.to_csv(os.path.join(DATA_FOLDER, 'categories.csv'), index=False)
df_orders.to_csv(os.path.join(DATA_FOLDER, 'orders.csv'), index=False)
df_reviews.to_csv(os.path.join(DATA_FOLDER, 'reviews.csv'), index=False)
df_user_buys_product.to_csv(os.path.join(DATA_FOLDER, 'user_buys_product.csv'), index=False)
df_order_contains_product.to_csv(os.path.join(DATA_FOLDER, 'order_contains_product.csv'), index=False)
df_product_belongs_to_category.to_csv(os.path.join(DATA_FOLDER, 'product_belongs_to_category.csv'), index=False)
df_user_writes_review.to_csv(os.path.join(DATA_FOLDER, 'user_writes_review.csv'), index=False)
