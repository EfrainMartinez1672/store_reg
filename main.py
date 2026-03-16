import valuer as df
from definition import name

name()

# Calculating the sum of the 'price' attribute/column
total = sum(df.price)


# Iterating through the 'update' attribute/column
for dc in df.update:
    print(dc)

print("valuer total: ", total)
