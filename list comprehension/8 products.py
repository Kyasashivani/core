products = {
"Laptop": 65000,
"Mouse": 500,
"Keyboard": 1500,
"Monitor": 12000
}
d={i:"Expensive" if products[i]>10000 else "Affordable" for i in products}
print(d)