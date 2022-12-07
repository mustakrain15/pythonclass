oil_price =[
    {
        "oil_type":"petrol",
        "prices":[
            {"year":2018,"price":100},
            {"year":2019,"price":100},
            {"year":2020,"price":180},
        ]
    },
    {
        "oil_type":"dieasl",
        "prices":[
            {"year":2018,"price":100},
            {"year":2019,"price":100},
            {"year":2020,"price":180},
        ]
    }

]


print("-"*50)
for oil in  oil_price:
    print(f"oil type :{oil.get('oil_type').capitalize()}")
    price =oil.get