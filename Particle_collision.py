
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def check_left_coll(position1_after):
    speed = 1
    edge_position = position1_after - 0.1
    
    if edge_position < 0:
        edge_position = -edge_position
        position1_after = edge_position + 0.1
        
        speed = -1
        
    return (position1_after, speed)


def check_right_coll(position2_after, box_size):
    speed = 1
    edge_position = position2_after + 0.1
    
    if edge_position > box_size:
        edge_position = box_size - (edge_position - box_size)
        position2_after = edge_position - 0.1

        speed = -1

    return (position2_after, speed)



def contact_point(pos1, pos2, velocity1, velocity2):
    adding = (pos2 - pos1)*(abs(velocity1)/(abs(velocity1) + abs(velocity2)))

    return pos1 + adding
    


def check_coll2(position1_before, position2_before, position1_after, position2_after, velocity1, velocity2, mass1, mass2):
    edge_position1 = position1_after + 0.1
    edge_position2 = position2_after - 0.1

    if edge_position1 > edge_position2:
        k = mass1/mass2
        m = k*velocity1 + velocity2
        n = k*(velocity1 ** 2) + velocity2**2

        center = contact_point(position1_before + 0.1, position2_before - 0.1, velocity1, velocity2)
        frame_left = (edge_position1 - center)/(position1_after - position1_before)
        
        velocity1 = (k*m - (m**2-(k+1)*(m**2-k*n))**0.5)/((k+1)*k)
        velocity2 = (m + (m**2 - (k+1)*(m**2-k*n))**0.5)/(k+1)

        edge_position1 = center + velocity1 * frame_left
        edge_position2 = center + velocity2 * frame_left

        position1_after = edge_position1 - 0.1
        position2_after = edge_position2 + 0.1
        
    return(position1_after, position2_after, velocity1, velocity2)


def simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size):
    ball1_x = [initial_pos1]
    ball2_x = [initial_pos2]

    velocity1 = initial_velocity1
    velocity2 = initial_velocity2

    for i in range(num_frames):
        position1_after = ball1_x[i] + velocity1
        velocity1 = velocity1 * check_left_coll(position1_after)[1]
        position1_after = check_left_coll(position1_after)[0]

        position2_after = ball2_x[i] + velocity2
        velocity2 = velocity2 * check_right_coll(position2_after, box_size)[1]
        position2_after = check_right_coll(position2_after, box_size)[0]

        position1_after_final = check_coll2(ball1_x[i], ball2_x[i], position1_after, position2_after, velocity1, velocity2, mass1, mass2)[0]
        position2_after_final = check_coll2(ball1_x[i], ball2_x[i], position1_after, position2_after, velocity1, velocity2, mass1, mass2)[1]
        velocity1_final = check_coll2(ball1_x[i], ball2_x[i], position1_after, position2_after, velocity1, velocity2, mass1, mass2)[2]
        velocity2_final = check_coll2(ball1_x[i], ball2_x[i], position1_after, position2_after, velocity1, velocity2, mass1, mass2)[3]


        velocity1 = velocity1_final
        velocity2 = velocity2_final

        ball1_x.append(position1_after_final)
        ball2_x.append(position2_after_final)

    createanimation(ball1_x, ball2_x, box_size)


def createanimation(positions1, positions2, boxsize):
    num_frames = len(positions1)

    fig, ax = plt.subplots()
    ax.set_xlim(0, boxsize)
    ax.set_ylim(-0.1, 0.1)

    ball1 , = ax.plot(positions1[0], 0,"bo", markersize=10)
    ball2 , = ax.plot(positions2[0], 0, "ro", markersize=10)

    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1, ball2
    
    ani = FuncAnimation(fig, update, frames=num_frames, blit=True)
    plt.show()

    plt.close(fig)

    return


initial_pos1 = 1
initial_pos2 = 2
initial_velocity1 = -0.1
initial_velocity2 = 0.1
mass1 = 1.0
mass2 = 1.5
num_frames = 100
box_size = 5


simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size)