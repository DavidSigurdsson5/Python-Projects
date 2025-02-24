import math

g = 9.82

while True:
    print("\nProjectile Motion Simulator")
    print("-" * 40)

    # Get valid user inputs
    while True:
        try:
            v0 = float(input("Enter the initial speed in m/s (must be > 0): "))
            if v0 > 0:
                break
            print("Invalid input. Speed must be greater than 0.")
        except ValueError:
            print("Invalid input. Enter a numerical value.")

    while True:
        try:
            angle = float(input("Enter the launch angle in degrees (0 < angle < 90): "))
            if 0 < angle < 90:
                break
            print("Invalid input. Angle must be between 0 and 90 degrees.")
        except ValueError:
            print("Invalid input. Enter a numerical value.")

    while True:
        try:
            dt = float(input("Enter the time step in seconds (must be > 0): "))
            if dt > 0:
                break
            print("Invalid input. Time step must be greater than 0.")
        except ValueError:
            print("Invalid input. Enter a numerical value.")

    # Convert degrees to radians
    theta = math.radians(angle)

    # Calculate initial velocity x og y
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)

    # Set starting point for variables
    x = 0
    y = 0
    t = 0

    # Print top of table
    print("\nTime (s)\tX (m)\t\tY (m)\t\tVx (m/s)\tVy (m/s)")
    print("-" * 50)

    # While loop
    while y >= 0:
        print(f"{t:.1f}\t\t{x:.4f}\t\t{y:.4f}\t\t{vx:.4f}\t\t{vy:.4f}")

        # Update values using equations
        t += dt
        x = vx * t
        y = (v0 * math.sin(theta) * t) - (0.5 * g * t**2)
        vy = v0 * math.sin(theta) - g * t  

    # Print final negative y value
    print(f"{t:.1f}\t\t{x:.4f}\t\t{y:.4f}\t\t{vx:.4f}\t\t{vy:.4f}")

    # Print The projectile has landed to end the table
    print("\nThe projectile has landed.")

    # Ask for repeat
    while True:
        retry = input("Would you like to run another simulation? (y/n): ").strip().lower()
        if retry in ['y', 'n']:
            break
        print("Invalid input. Enter 'y' for yes or 'n' for no.")

    if retry == 'n':
        break



