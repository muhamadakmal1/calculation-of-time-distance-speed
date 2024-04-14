def calculate_speed_distance_time():
    print("Welcome to Speed, Distance, Time Calculator!")
    print("Please choose what you want to calculate:")
    print(" Speed")
    print(" Distance")
    print(" Time")
    choice = input("Enter your choice (1/2/3): ")

    if choice == 'speed':
        distance = float(input("Enter distance (in units): "))
        time = float(input("Enter time (in units): "))
        speed = distance / time
        print("Speed:", speed, "units per unit of time")
    elif choice == 'distance':
        speed = float(input("Enter speed (in units per unit of time): "))
        time = float(input("Enter time (in units): "))
        distance = speed * time
        print("Distance:", distance, "units")
    elif choice == 'time':
        distance = float(input("Enter distance (in units): "))
        speed = float(input("Enter speed (in units per unit of time): "))
        time = distance / speed
        print("Time:", time, "units")
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")

calculate_speed_distance_time()
