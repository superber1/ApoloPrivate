
import random
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, position: list, num:int) -> None:
        self._position = position
        self._num = num

    def get_position(self):
        return self._position

    def set_position(self, pos:list):
        self._position = pos

    def travel(self, path:int):
        self._position.append(self._position[len(self._position) - 1] + path)

    def get_num(self):
        return self._num


def new_particle(pos, i):
    return Particle(pos, i)


def random_walk(num_steps, prob_right, num_particles):
    particles_list = []
    start_list = [0]


    i = 0
    while i < num_particles:
        particles_list.append(new_particle(start_list.copy(), i))
        i += 1

    for x in range(num_steps):
        for y in particles_list:
            prob = random.random()
            if(prob > prob_right):
                y.travel(-1)
            else:
                y.travel(1)

    particle_paths = []

    for particle in particles_list:
        particle_paths.append(particle.get_position())
    
    createplot(num_steps, particle_paths)
    
    return particle_paths

def createplot(num_steps, particle_paths):
    time = [x for x in range(len(particle_paths[0]))]
    #Build the plot with all the particles
    for particle_path in particle_paths:
        plt.plot(particle_path, time)

    plt.title("Random Walk - N particles")
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.show()

num_steps = 100
prob_right = 0.5
num_particles = 10

random_walk(num_steps, prob_right, num_particles)