import sys

def component(t, pos, vel):
  value = 0
  N = len(pos)
  for k in range(0, N):
    value += (pos[k] + t * vel[k])
  return value / N

def components(x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, t):
  return component(t, x_pos, x_vel), component(t, y_pos, y_vel), component(t, z_pos, z_vel)

def sum_of_squares(Xm, Ym, Zm):
  return Xm ** 2 + Ym ** 2 + Zm ** 2

def Dt(x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, t):
  Xm, Ym, Zm = components(x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, t)
  return sum_of_squares(Xm, Ym, Zm) ** 0.5

num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
  num_flies = int(sys.stdin.readline())
  x_pos = []
  y_pos = []
  z_pos = []
  x_vel = []
  y_vel = []
  z_vel = []
  for k in range(1, num_flies + 1):
    fly = list(map(float,sys.stdin.readline().split()))
    x_pos.append(fly[0])
    y_pos.append(fly[1])
    z_pos.append(fly[2])
    x_vel.append(fly[3])
    y_vel.append(fly[4])
    z_vel.append(fly[5])
  t_min = 0.0
  denom = sum_of_squares(sum(x_vel), sum(y_vel), sum(z_vel)) 
  if denom != 0.0:
    t_min = -1 * (sum(x_pos) * sum(x_vel) + sum(y_pos) * sum(y_vel) + sum(z_pos) * sum(z_vel)) / denom
  if t_min < 0.0:
    t_min = 0.0
  d_min = Dt(x_pos, y_pos, z_pos, x_vel, y_vel, z_vel, t_min)
  print("Case #" + str(case) + ":", d_min, t_min) 

