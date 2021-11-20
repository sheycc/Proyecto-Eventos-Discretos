from utils import *
from random import choice  

# Simulation
def sim(t, rnd = False):
    t_sim, n_a, bag = 0, 0, []
    a = dict([(i, []) for i in range(5)])
    d = dict([(i, []) for i in range(5)])
    track_info = dict([(i, 0) for i in range(5)])

    t_a = expo_distribution(1/20)
    t_d = dict([(i, 2**32) for i in range(5)])

    f = open('./airport_sim.txt', 'w')
    f.writelines(f"~~~~~~~~~~~~~~~~~~~~~~~~ Barajas Airport Simulation ~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
    f.writelines(f"## Start simulation:\n")
    while 1:
        if min(t_a, t_sim, *t_d.values()) > t:
            break
        if t_a == min(t_a, *t_d.values()):
            n_a += 1
            t_sim = t_a
            f.writelines(f"~~> Minute: {t_sim} \n")
            f.writelines(f"          - Airplane {n_a} arrive to the airport.\n")
            t_a = t_sim + expo_distribution(1/20)

            available = [p_id for p_id, a_id in track_info.items() if a_id == 0]
            if available:
                i = available[0] if not rnd else choice(available)
                a[i].append(t_sim)
                track_info[i] = n_a
                f.writelines(f"~~> Minute: {t_sim} \n")
                f.writelines(f"          - Airplane {track_info[i]} comes into landingtrack {i + 1}.\n")
                
                # call v.a 
                norm_dist = norm_distribution(10, 5) + norm_distribution(10, 5)
                expo_dist_inv = expo_distribution(1/15) * unif_distribution([(0, 0.9), (1, 0.1)]) 
                y = norm_dist + expo_dist_inv + max(expo_distribution(1/30), expo_distribution(1/30))
                t_d[i] = y + t_sim

            else:
                f.writelines(f"~~> Minute: {t_sim} \n")
                f.writelines(f"          - Airplane {n_a} waiting to come in.\n")
                bag.append(n_a)
        else:
            t_sim = min(t_d.values())
            p = [p_id for p_id, q in t_d.items() if q == t_sim][0]
            d[p].append(t_sim)
            f.writelines(f"~~> Minute: {t_sim} \n")
            f.writelines(f"          - Airplane {track_info[p]} leave landingtrack {p + 1}.\n")
            track_info[p], t_d[p] = 0, 2**32

            if len(bag) > 0:
                tmp = bag.pop(-1)
                a[p].append(t_sim)
                track_info[p] = tmp
                f.writelines(f"~~> Minute: {t_sim} \n")
                f.writelines(f"          - Airplane {track_info[p]} comes into landingtrack {p + 1}.\n")

                # call v.a
                norm_dist = norm_distribution(10, 5) + norm_distribution(10, 5)
                expo_dist_inv = expo_distribution(1/15) * unif_distribution([(0, 0.9), (1, 0.1)])
                y = norm_dist + expo_dist_inv + max(expo_distribution(1/30), expo_distribution(1/30))
                t_d[p] = y + t_sim

    f.writelines(f"## End simulation.\n")
    f.close()
    return a, d