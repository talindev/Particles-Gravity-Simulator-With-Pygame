import pygame
import random
import math
import numpy as np
from customtkinter import *


# GLOBAL VARIABLES --------------
x1 = 0
y1 = 0
vx1 = 0
vy1 = 0
m1 = 0
x2 = 0
y2 = 0
vx2 = 0
vy2 = 0
m2 = 0
# -------------------------------

# GUI fraction with CustomTkinter ----------------
# CTK Setup
app = CTk()
app.geometry('1920x1080')
app.title('Entries field')
app.after(0, lambda: app.state('zoomed'))
# Function to be executed when the button is pressed, collecting what the user typed on the entry fields
def button_callback():
    global x1,y1,vx1,vy1,m1,x2,y2,vx2,vy2,m2
    if fun_mode_activator():
        pass
    elif not fun_mode_activator() and check_randomize_values():
        x1 = e_x1.get()
        y1 = e_y1.get()
        vx1 = e_vx1.get()
        vy1 = e_vy1.get()
        m1 = e_m1.get()
        x2 = e_x2.get()
        y2 = e_y2.get()
        vx2 = e_vx2.get()
        vy2 = e_vy2.get()
        m2 = e_m2.get()
    else:
        x1 = random.randint(1, 999)
        y1 = random.randint(1, 719)
        vx1 = random.randint(-4, 4)
        vy1 = random.randint(-4, 4)
        m1 = random.randint(1, 50)
        x2 = random.randint(1, 999)
        y2 = random.randint(1, 719)
        vx2 = random.randint(-4, 4)
        vy2 = random.randint(-4, 4)
        m2 = random.randint(1, 50)

    # Lastly, closes the interface
    app.destroy()

# If checked, draws vector lines
def check_vector_lines():
    global check_vector
    check_vector = vector_checkbox.get()
    return check_vector

# If checked, draws distance line between the particles
def check_distance_line():
    global check_dist
    check_dist = dist_checkbox.get()
    return check_dist

# If checked, randomizes all values
def check_randomize_values():
    global check_random
    check_random = random_checkbox.get()

# Activates fun mode :)
def fun_mode_activator():
    global check_fun_mode
    check_fun_mode = fun_checkbox.get()
    return check_fun_mode

# Labels and entries
label_p1 = CTkLabel(master=app, text='Particle 1')
e_x1 = CTkEntry(master=app, placeholder_text='Initial X Position')
e_y1 = CTkEntry(master=app, placeholder_text='Initial Y Position')
e_vx1 = CTkEntry(master=app, placeholder_text='Initial X-axis Velocity')
e_vy1 = CTkEntry(master=app, placeholder_text='Initial Y-axis Velocity')
e_m1 = CTkEntry(master=app, placeholder_text='Initial Mass')
label_p2 = CTkLabel(master=app, text='Particle 2')
e_x2 = CTkEntry(master=app, placeholder_text='Initial X Position')
e_y2 = CTkEntry(master=app, placeholder_text='Initial Y Position')
e_vx2 = CTkEntry(master=app, placeholder_text='Initial X-axis Velocity')
e_vy2 = CTkEntry(master=app, placeholder_text='Initial Y-axis Velocity')
e_m2 = CTkEntry(master=app, placeholder_text='Initial Mass')

# Optional checks
vector_checkbox = CTkCheckBox(master=app, text="Enable vector lines", command=check_vector_lines, onvalue=True, offvalue=False)
dist_checkbox = CTkCheckBox(master=app, text="Enable distance line", command=check_distance_line, onvalue=True, offvalue=False)
random_checkbox = CTkCheckBox(master=app, text="Randomize values!", command=check_randomize_values, onvalue=True, offvalue=False)

# Fun mode :)
fun_checkbox = CTkCheckBox(master=app, text="Fun mode :)", command=fun_mode_activator, onvalue=True, offvalue=False, hover_color='pink', border_color='red', checkmark_color='red')

# Command button
button = CTkButton(master=app, text='Send All!', command=button_callback)

# Tip to help the users base their values around those numbers
recommendation1 = CTkLabel(master=app, text='Hey! Here\'s a tip:')
recommendation2 = CTkLabel(master=app, text='These following values give you a stable orbit at G = 100. Try playing around with them..')
recommendation3 = CTkLabel(master=app, text='Particle 1: x1 = 250 / y1 = 360 / vx1 = 0 / vy1 = 1 / m1 = 10')
recommendation4 = CTkLabel(master=app, text='Particle 2: x1 = 750 / y1 = 360 / vx1 = 0 / vy1 = -1 / m1 = 10')

# Interface packing
label_p1.pack()
e_x1.pack(expand=False, padx=10, pady=5)
e_y1.pack(expand=False, padx=10, pady=5)
e_vx1.pack(expand=False, padx=10, pady=5)
e_vy1.pack(expand=False, padx=10, pady=5)
e_m1.pack(expand=False, padx=10, pady=5)
label_p2.pack()
e_x2.pack(expand=False, padx=10, pady=5)
e_y2.pack(expand=False, padx=10, pady=5)
e_vx2.pack(expand=False, padx=10, pady=5)
e_vy2.pack(expand=False, padx=10, pady=5)
e_m2.pack(expand=False, padx=10, pady=5)
vector_checkbox.pack(padx=10, pady=5)
dist_checkbox.pack(padx=10, pady=5)
random_checkbox.pack(padx=10, pady=5)
fun_checkbox.pack(padx=15,pady=30)
button.pack(padx=10, pady=5)
recommendation1.pack(padx=10, pady=5)
recommendation2.pack(padx=10, pady=5)
recommendation3.pack(padx=10, pady=5)
recommendation4.pack(padx=10, pady=5)

# Runs the interface loop
app.mainloop()

# ----------------------------------------------

# Initializing pygame
pygame.init()

# Basic "constants"
BLACK = (0,0,0)
GREEN = (0, 255, 0)
BLUE = (0,0,255)
WIDTH = 1000
HEIGHT = 720

# Creating the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Creating the particle class
class Particle:
    # Creating the init function with the positional, cinematic and mass instance attributes
    def __init__(self, x, y, vx, vy, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
    
    # Updates the particle's position on the screen based on it's velocity in each axis
    def update(self):
        self.x += self.vx
        self.y += self.vy
        # Reduced acceleration over time
        self.vx -= 0.01
        self.vy -= 0.01
    
    def draw(self):

        # Draws the particle
        pygame.draw.circle(screen, GREEN, (self.x,self.y), self.mass)

    def draw_vectors(self):

        # Drawing vector line for monitoring the particles velocity vectors
        pygame.draw.line(screen, GREEN, (self.x, self.y), (self.x + self.vx * 10, self.y + self.vy * 10)) # TODO: ctkinter option to print the lines
    
    def draw_dist(self, other):

        # Drawing line between particles centers to monitor the distance between them
        pygame.draw.line(screen, BLUE, (self.x, self.y), (other.x, other.y))

# Function that checks for any collisions, calculates the overlap of the collision and alters the particles velocities module and direction based on the overlap
def collision(particles):
    # Iterates over the particles list
    for i in range(len(particles)):
        p1 = particles[i]
        for j in range(i + 1, len(particles)):
            p2 = particles[j]

            # 2 Particles overlap when their distance is numerically smaller than the sum of their radii
            if (p2.x - p1.x)**2 + (p2.y - p1.y)**2 < ((p1.mass)**2 + (p2.mass)**2):

                # Calculating their new velocities based on conservation of linear momentum and kinetic energy
                v1x = ((p1.mass - p2.mass) * p1.vx + 2 * p2.mass * p2.vx) / (p1.mass + p2.mass)
                v1y = ((p1.mass - p2.mass) * p1.vy + 2 * p2.mass * p2.vy) / (p1.mass + p2.mass)
                v2x = ((p2.mass - p1.mass) * p2.vx + 2 * p1.mass * p1.vx) / (p1.mass + p2.mass)
                v2y = ((p2.mass - p1.mass) * p2.vy + 2 * p1.mass * p1.vy) / (p1.mass + p2.mass)

                # Updating velocities for each axis
                p1.vy = v1y
                p2.vx = v2x
                p2.vy = v2y
                p1.vx = v1x

# Function that checks if the particle's coordinates exceeds the screen limits, one particle at a time
def collision_border(p):
    if p.x <= 0 or p.x >= WIDTH:
        p.vx *= -1
    if p.y <=0 or p.y >= HEIGHT:
        p.vy *= -1
            
# Gravity calculations with newtonian mechanics and law of gravitation -----------------------------------------

# Calculates the distance between the particles using the distance on each axis and lastly using the Pythagoras Theorem
def calc_dist(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    dist = math.sqrt(dx**2 + dy**2)
    return dx, dy, dist

# Calculates the directions of the particles dividing their distances and each axis by the overall distance previously calculated
def calc_dir(dx, dy, dist):
    dirx = dx / dist
    diry = dy / dist
    return dirx, diry

# Finally, reunites the previously calculated parameters and calculates the gravitational force between the particles, so it can alter their velocities based on the force
# between them! The hard-coded gravitational constant here is 100.
def gravity(particles):
    for i in range(len(particles)):
        p1 = particles[i]
        for j in range(i + 1, len(particles)):
            p2 = particles[j]
            dx, dy, dist = calc_dist(p1, p2)
            dirx, diry = calc_dir(dx, dy, dist)

            if dist == 0:
                continue

            G = 100
            f = G * (p1.mass * p2.mass) / dist**2
            p1.vx += f * dirx / p1.mass
            p1.vy += f * diry / p1.mass
            p2.vx -= f * dirx / p2.mass
            p2.vy -= f * diry / p2.mass

# --------------------------------------------------------------------------------------------------------------

# Calculates the particle's kinetic energy one particle at a time, using the particle's overall velocity, initially calculated with Pythagoras Theorem
# then multiplied by the particle's mass and divided by 2. Lastly, the function returns the kinetic energy of the given particle
def kinetic_energy(p):
    v = math.sqrt(p.vx**2 + p.vy**2)
    KE = (p.mass * v**2) / 2

    return KE

# Calculates the particle's potential gravitational energy, using the formula listed below.
# Iterating in nested for loops, the function calculates the overall distance between the particles using Pythagoras Theorem.
# Lastly, minus the gravitational constant times the first particle's mass times the second particle's mass is divided by the overall distance
# Finally, the function returns the potential gravitational energy of the given particle
def potential_energy(particles):
    for i in range(len(particles)):
        p1 = particles[i]
        for j in range(i + 1, len(particles)):
            p2 = particles[j]

            G = 100
            dx = p2.x - p1.x
            dy = p2.y - p1.y
            d = math.sqrt(dx**2 + dy**2)
            PE = -(G*p1.mass*p2.mass) / d

            return PE

# Initializing lists
particles = []
kinetic_energy_list1 = []
kinetic_energy_list2 = []
kinetic_energy_list3 = []
kinetic_energy_list4 = []
kinetic_energy_list5 = []
kinetic_energy_list6 = []
kinetic_energy_list7 = []
kinetic_energy_list8 = []
kinetic_energy_list9 = []
kinetic_energy_list10 = []
potential_energy_list = []

# Main loop
def main():
    # Initializes the particle quantity limit with the bool False
    limit = False
    fun_mode_limit = False
    # Initializes the pygame clock for fps counting and runs the program
    clock = pygame.time.Clock()
    run = True
    while run:
        # Game quit checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        screen.fill(BLACK)

        # Fun mode functionality
        if fun_mode_activator():
            # Creates 10 particles
            if len(particles) < 10:
                for i in range(10 - len(particles)):
                    p = Particle(random.randint(1, 999), random.randint(1, 719), random.randint(-4, 4), random.randint(-4, 4), random.randint(1, 50))
                    particles.append(p)

            # Executing previously created functions
            # To prevent unwanted acceleration when handling collisions, the order here matters!
            gravity(particles)
            collision(particles)

            for i in range(len(particles)):
                collision_border(particles[i])

            # Appending values to a list so numpy could calculate the variance of the list
            kinetic_energy_list1.append(kinetic_energy(particles[0]))
            kinetic_energy_list2.append(kinetic_energy(particles[1]))
            kinetic_energy_list3.append(kinetic_energy(particles[2]))
            kinetic_energy_list4.append(kinetic_energy(particles[3]))
            kinetic_energy_list5.append(kinetic_energy(particles[4]))
            kinetic_energy_list6.append(kinetic_energy(particles[5]))
            kinetic_energy_list7.append(kinetic_energy(particles[6]))
            kinetic_energy_list8.append(kinetic_energy(particles[7]))
            kinetic_energy_list9.append(kinetic_energy(particles[8]))
            kinetic_energy_list10.append(kinetic_energy(particles[9]))
            potential_energy_list.append(potential_energy(particles))


            # For each particle in the particles list, updates and draws the particle's circle
            for particle in particles:
                particle.update()
                particle.draw()
                if check_vector_lines():
                    particle.draw_vectors()
                if check_distance_line():
                    for i in range(1, len(particles)):
                        particles[i-1].draw_dist(particles[i])

            # FPS Counting
            pygame.display.flip()
            clock.tick(60)

        # Normal mode loop
        else:
            # If the limit has not been reached before, 2 particles are created with the constructor function on each with the user's typed data, converted each to floating points
            if not limit:
                p1 = Particle(float(x1), float(y1), float(vx1), float(vy1), float(m1)) # Particle(250, 360, 0, 1, 10)
                p2 = Particle(float(x2), float(y2), float(vx2), float(vy2), float(m2)) # Particle(750, 360, 0, -1, 10)
                # The created particles are appended to the particles list
                particles.append(p1)
                particles.append(p2)
                # The limit is reached and activated so this loop would not be executed again
                limit = True
            else:
                # Executing previously created functions
                # To prevent unwanted acceleration when handling collisions, the order here matters!
                gravity(particles)
                collision(particles)

                collision_border(p1)
                collision_border(p2)

                # Appending values to a list so numpy could calculate the variance of the list
                kinetic_energy_list1.append(kinetic_energy(p1))
                kinetic_energy_list2.append(kinetic_energy(p2))
                potential_energy_list.append(potential_energy(particles))

                # For each particle in the particles list, updates and draws the particle's circle
                for particle in particles:
                    particle.update()
                    particle.draw()
                    if check_vector_lines():
                        particle.draw_vectors()
                    if check_distance_line():
                        p1.draw_dist(p2)

                # FPS Counting
                pygame.display.flip()
                clock.tick(60)
    
    # Quitting event
    pygame.quit()

    # Ending interface - setup
    ending = CTk()
    ending.geometry('1920x1080')
    ending.title('Simulation results')
    ending.after(0, lambda: ending.state('zoomed'))

    # Showing the results of the simulation
    KE_p1 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 1: {np.var(kinetic_energy_list1)}")
    KE_p2 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 2: {np.var(kinetic_energy_list2)}")

    # Fun mode labels
    KE_p3 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 3: {np.var(kinetic_energy_list3)}")
    KE_p4 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 4: {np.var(kinetic_energy_list4)}")
    KE_p5 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 5: {np.var(kinetic_energy_list5)}")
    KE_p6 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 6: {np.var(kinetic_energy_list6)}")
    KE_p7 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 7: {np.var(kinetic_energy_list7)}")
    KE_p8 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 8: {np.var(kinetic_energy_list8)}")
    KE_p9 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 9: {np.var(kinetic_energy_list9)}")
    KE_p10 = CTkLabel(master=ending, text=f"Kinetic energy variance on particle 10: {np.var(kinetic_energy_list10)}")

    # Gravitational potential energy between all of the particles
    PE_ps = CTkLabel(master=ending, text=f"Gravitational potential energy variance between the particles: {np.var(potential_energy_list)}")

    # Final tip
    instruction = CTkLabel(master=ending, text="To form a stable orbit, you have to adjust the values so the kinetic energies and potential energy are as less oscilant as possible!")

    # Interface packing
    KE_p1.pack(padx=10,pady=15)
    KE_p2.pack(padx=10,pady=15)
    # Packs more information depending if fun mode was activated
    if fun_mode_activator():
        KE_p3.pack(padx=10,pady=15)
        KE_p4.pack(padx=10,pady=15)
        KE_p5.pack(padx=10,pady=15)
        KE_p6.pack(padx=10,pady=15)
        KE_p7.pack(padx=10,pady=15)
        KE_p8.pack(padx=10,pady=15)
        KE_p9.pack(padx=10,pady=15)
        KE_p10.pack(padx=10,pady=15)
    PE_ps.pack(padx=10,pady=15)
    instruction.pack(padx=10,pady=15)

    # Running the ending frame's main loop
    ending.mainloop()

# Prevents the main function from being executed if imported by another program
if __name__ == "__main__":
    main()
