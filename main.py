import valuer as df
from definition import name

name()
total = sum(df.price)
print("--Daily sales summary--")
for dc in df.update:
    print(dc)
print("valuer total: ", total) 
