# Particles Gravity Simulator
# Context

Once i was done with CS50P's lectures, it was time to finally put my hands into real work, and create a personal project, from dust.

I used 1 or 2 days to confirm what i was going to do, but to be fair, i already had an idea of what was going to be done.

That was until i finally settled and decided the theme was going to be a Star Collider w/ Eulerian Fluids, i had seen a NASA video on 2 neutron stars colliding in a computer simulation, and i thought it was awesome! I always were an astronomy enthusiast, taking the Brazil's Official Astronomy and Astronautics Olympiad 2 times in the past, and passing.

So with the "perfect" idea in mind, i traced a diagram with theory and libraries that would come in handy for my project.
But sometimes things do not go as expected.

I studied for 1 day some dynamics, particle motion and fluids. Then i  got right into the code part. I did not use any physics engines, and that is the fact that made everything difficult.

My biggest difficulty was implementing gravitational physics between the particles. And once i got through this, i humbled myself to stick with this, and just implement some features along the gravity physics.

# project.py: Introduction


There are 2 main features in my project: UI (User Interface) and the simulator.

As the UI is only a way to perfect the user's experience, i will start and focus mainly in the gravity engine itself, made through pygame.

In the code, pygame is initialized, and the constants responsible for colors (BLACK, GREEN, BLUE) and the pygame's window (WIDTH, HEIGHT) are declared. The simulator's main screen is created through ```pygame.display.set_mode((WIDTH,HEIGHT))```.
Then, a ```Particle``` ```class``` is created, initializing the particle through ```__init__()```, creating instance variables ```x```, ```y```, ```vx```, ```vy``` and ```mass```.

The choice for a ```class``` is due to the facility of storing and acessing the particle's properties.

Through the ```class```, some methods are created for the particle's functionality. ```update()``` will change the particle's position in the pygame screen at each loop iteration incremeating the ```x``` and ```y``` values with the ```vx``` and ```vy``` values, and with that, ```update()``` will also decrease the particle's velocity in each axis by 0.01 at each loop iteration, to prevent the particle's from maintaining absurd speeds.

```draw()```, as the name suggests, will draw the particle in the screen, with a green color, and taking the particle's mass as it's radius.

the optional methods ```draw_vectors()``` and ```draw_dist()``` will draw lines to indicate visually the particle's speed and direction (through the vector's direction and size) and the distance between 2 or more particles.
# project.py: Main Physics

The main functions (outside other functions or classes) are ```collision()```, ```collision_border()```, ```calc_dist()```, ```calc_dir()``` and ```gravity()```.

```collision()``` takes a list of particles, where it will iterate through a given particle and the particle next to it, check if they are overlapping **(particles overlap when the distance between their centers is smaller than the sum of their radii)**. It will check for this condition calculating the distance in a cartesian plane and comparing it to the sum of each radius squared.
$$
d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}
$$
##### Code 'if' statement:
```if (p2.x - p1.x)**2 + (p2.y - p1.y)**2 < ((p1.mass)**2 + (p2.mass)**2)```
If the collision is confirmed, the particle's velocities are updated conform to the conservation of linear momentum ($p$) and kinetic energy ($k$) in elastic collisions, in which the velocities between 2 particles are swapped.
$$
p = mv
$$

$$
p_{1initial} + p_{2initial} = p_{1final} + p_{2final}
$$

$$
k = \frac{1}{2}mv^2
$$

$$
\frac{1}{2}m_{1initial}{v_{1initial}}^2 + \frac{1}{2}m_{2initial}{v_{2initial}}^2 = \frac{1}{2}m_{1final}{v_{1final}}^2 + \frac{1}{2}m_{2final}{v_{2final}}^2
$$

$$
\therefore v_{1xfinal} = \frac{(m_1 - m_2)v_{1xinitial}+2m_2v_{2xinitial}}{m_1+m_2}
$$

$$
\therefore v_{1yfinal} = \frac{(m_1 - m_2)v_{1yinitial}+2m_2v_{2yinitial}}{m_1+m_2}
$$

$$
\therefore v_{2xfinal} = \frac{(m_2 - m_1)v_{2xinitial}+2m_1v_{1xinitial}}{m_1+m_2}
$$

$$
\therefore v_{2yfinal} = \frac{(m_2 - m_1)v_{2yinitial}+2m_1v_{1yinitial}}{m_1+m_2}
$$

Finally, each velocity is updated with the new calculated velocities.

```
p1.vy = v1y
p2.vx = v2x
p2.vy = v2y
p1.vx = v1x
```

```collision_border()``` is a simpler version of ```collision()```, checking if the particle's x and y coordinates exceed the previously declared screen constants (WIDTH, HEIGHT), if confirmed, the particle's velocity in the exceeded axis is inverted.

```
if p.x <= 0 or p.x >= WIDTH:

        p.vx *= -1

if p.y <=0 or p.y >= HEIGHT:

        p.vy *= -1
```

### Gravity main engine

Initially, ```calc_dist()``` receives 2 particles, calculates their cartesian distances through the distance formula previously mentioned, and returns the distance in the x-axis (```dx```), distance in the y-axis (```dy```), and the overall cartesian distance (```dist```).

Then, ```calc_dir()``` receives the returned values from ```calc_dist()``` and normalizes the vectors, returning their directions.

$$
dir_x,dir_y = (\frac{dx}{d},\frac{dy}{d})
$$
Going further, we reach the main gravity motor.

```gravity()``` receives a particle list, iterating over it and 'grabbing' the first and it's next particle in the list (```p1```,```p2```), then, the function calls the previous functions inside it, storing the returned values in matching variables, and also preventing the distance from being 0, to prevent ```ZeroDivisionError```.
\
Finally, the function declares a gravitational constant (```G```), with a value of $100$, and applies the masses, distances and the constant in the Newton's law of gravity, storing the gravitational force between the particles in the variable ```f```.

$$
f = \frac{G\cdot (m_1\cdot m_2)}{d^2}
$$

Then, the force is applied for each particle's axial velocity, increasing/decreasing the velocity by the force times the normalized direction in the refering axis, all divided by the particle's mass.

$$
v_{1x} = \frac{f\cdot dir_x}{m_1}
$$

$$
v_{1y} = \frac{f\cdot dir_y}{m_1}
$$

$$
v_{2x} = \frac{f\cdot dir_x}{m_2}
$$

$$
v_{2y} = \frac{f\cdot dir_y}{m_2}
$$

The velocities are then updated in opposed directions.

```
p1.vx += v1x
p1.vy += v1y
p2.vx -= v2x
p2.vy -= v2y
```

### Statistical functions

The 2 functions that return statistical numbers are ```kinetic_energy()``` and ```potential_energy()```.

```kinetic_energy()``` receives a single particle, and process the particle's overall velocity and mass through the kinetic energy ($k$) formula to return the particle's quantity of motion energy and return it.

$$
v = \sqrt{v_x^2 + v_y^2}
$$

$$
k = \frac{m\cdot v^2}{2}
$$

```potential_energy()``` in the other hand receives a list of particles, storing 2 particles next to each other in the list, processing their distances (cartesian distance and the distance in each axis), masses with the gravitational constant through the potential gravitational energy ($U$) to calculate the resulting energy from their gravitational interactions and return it.

$$
U = \frac{-(G\cdot m_1\cdot m_2)}{d}
$$

# project.py: Main Loop

The project's main loop (```main()```) is basically executing pygame.

Firstly, boolean variables are put to ```False```, the ```pygame.time.Clock()``` function is stored in the ```clock``` variable for better control of the Frames Per Second (FPS), and pygame is ran.

While running, it repeatly checks if the user closes the window, and if so, this breaks from the loop.

The screen is filled with the black color (```screen.fill(BLACK)```), and the program checks if 'fun mode' is activated, in which 10 particles are summoned with random values each, and the general physics is executed.

If not activated, there will only be 2 particles, with random values or not, by user's choice in the start UI.

After the 2 particles are summoned by a constructor call to the ```Particle``` ```class```,  they are appended to the ```particles``` list initialized empty before the main loop. Once there are 2 particles, the ```limit``` variable is set to ```True``` and the particle creation action is stopped.

Using the previously created physics functions, the loop will execute the gravitational accelerations on each particles and then later check for collisions between them.

Collisions with the window's borders are also checked.

For further shown statistics, the kinetic energy of each particle and the potential gravitational energy of their interactions is stored in designed lists. These large quantities of data are stored in lists so the variance is later calculated by the ```numpy``` package.

Also, for each ```particle``` stored in the ```particles``` list, the refering particle is updated and drawn in the screen using the ```update()``` and ```draw()``` methods. If checked previously, the vector and distance lines are also drawn by the ```draw_vectors()``` and ```draw_dist()``` methods.

Finally, all of this content is updated on the screen by the ```pygame.display.flip()``` function and the FPS is counted by the ```clock.tick(60)``` function, using 60 Frames Per Second (60 FPS).

# project.py: User Interface

Briefly speaking, the values and checks are previously chosen by the user by a UI (User Interface). I chose to use ```customtkinter``` because of the facility, modern touch and readability of the UI.

## Start UI

The first window to appear once the user runs the project.py file is the start UI. It gives the option to choose each value of the particles 1 and 2, to draw the vector and distance lines, and to toggle 'fun mode'. There is also a configuration for a stable orbit below.

## Ending UI

The last window to appear once the user quits the pygame window is the ending UI. It displays all of the particle's kinetic energy and potential gravitational energy variations as well as a final tip to simulating stable orbits between the particles.

# project.py: Conclusion

This was it! I loved implementing this project, even though i had tons of headache and stress doing it. But that is how life works, isn't it?

Im glad to present this to the world.

It has my personality in it. And i love it.

Thank you! :)


Yours sincerely,
talindev
