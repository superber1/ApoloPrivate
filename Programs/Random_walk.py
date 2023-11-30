
import random
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, position) -> None:
        self.position = position


def random_walk(num_steps, prob_right, num_particles):
    


    createplot(num_steps, particle_paths)
    
    return particle_paths

def createplot(num_steps, particle_paths):
    time = [x for x in range(len(particle_paths[0]))]
    # Build the pl o t with a l l the p a r t i c l e s
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