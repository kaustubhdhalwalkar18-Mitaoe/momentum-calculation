# Momentum Calculator
# Formula: p = m * v

def calculate_momentum(mass, velocity):
    """
    Calculates the momentum of an object.

    Parameters:
    mass (float): Mass in kilograms
    velocity (float): Velocity in meters per second

    Returns:
    float: Momentum in kg·m/s
    """
    return mass * velocity


def main():
    print("=== Momentum Calculator ===")

    try:
        mass = float(input("Enter mass (in kg): "))
        velocity = float(input("Enter velocity (in m/s): "))

        momentum = calculate_momentum(mass, velocity)

        print(f"\nMomentum of the object: {momentum} kg·m/s")

    except ValueError:
        print("❌ Please enter valid numeric values.")


if __name__ == "__main__":
    main()
