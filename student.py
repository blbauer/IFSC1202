# Israel Davidson
# Exam Two Project - Car Sales Data Analysis

        # Read car sales data from file
car_sales_list = {}
with open("CarSales.txt", "r") as file:
    for line in file:
        car_data = line.strip().split(",")
        car_brand = car_data[0]
        car_sales_list[car_brand] = {
            "make": car_data[0],
            "price": float(car_data[1])
        }

# Calculate overall statistics
total_cars = len(car_sales_list)
total_price = sum(car["price"] for car in car_sales_list.values())
average_price = total_price / total_cars if total_cars > 0 else 0
print(f"Total number of cars - average price: {total_cars} - ${average_price:.2f}")

# Prompt user for a car brand to search
search_brand = input("Enter Car Brand to search for statistics: ")
if search_brand in car_sales_list:
    car_info = car_sales_list[search_brand]
    cars_sold = car_info["quantity_sold"]
    average_price_make = car_info["price"]
# Calculate percentage difference
percentage = ((average_price_make - average_price) / average_price) * 1000 if average_price != 0 else 0

print(f"{cars_sold} Cars Sold")
print(f"${average_price_make} Average Price")

if percentage >= 0:
    print(f"{percentage:.2f}% Above Average")
else:
    print(f"{percentage:.2f}% Below Average")

#if __name__ == "__main__":
#main()
    
        # Loop to allow multiple searches until user types blank car brand entry
while True:
    search_brand=input("Enter Car Brand to search for statistics (or blank entry to quit): ")
    if search_brand=="":
        break
    # Convert to uppercase for case-insensitive search
    search_brand=search_brand.upper()
    if search_brand in car_sales_list:
        car_info=car_sales_list[search_brand]
        print(f"Car Brand: {search_brand}, Make: {car_info['make']}, Price: ${car_info['price']:.2f}, Quantity Sold: {car_info['quantity_sold']}")
    else:
        print("Car Brand not found.")

# Calculate and print total sales for each car
for car_brand, car_info in car_sales_list.items():
    total_sales=car_info["price"]*car_info["quantity_sold"]
    print(f"Car Brand: {car_brand}, Make: {car_info['make']}, Total Sales: ${total_sales:.2f}")


