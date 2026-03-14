import valuer as df
from definition import name

# Calculating the sum of the 'price' attribute/column
total = sum(df.price)

print(f"--Daily sales summary for {name}--")

# Iterating through the 'update' attribute/column
for dc in df.update:
    print(dc)

print("valuer total: ", total)
