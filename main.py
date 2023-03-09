# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# 1
def greet(name, greeting='Hello, <name>!'):

    replaced_name = greeting.replace("<name>", name)

    return replaced_name

print(greet("Rick"))
print(greet("Bob", "What's up"))

# 2
def force(mass, body='earth'):
    planet_gravity = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        'earth': 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58
    }

    force = mass * planet_gravity[body]
    rounded_force = round(force)

    return rounded_force

print(force(7, "neptune"))

# 3
def pull(m1, m2, d):

    g = 6.674 * (10**-11)
    force = g * (m1 * m2) / d ** 2

    return force

print(pull(800, 1500, 3))
