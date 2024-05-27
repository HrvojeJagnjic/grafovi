import math
import matplotlib.pyplot as plt

def hitac(v0, alfa):
    g=9.81
    t_max=round(2*v0*math.sin(math.radians(alfa))/g, 1)
    x=[]
    y=[]
    alfa_r=math.radians(alfa)
    for t in range(int(t_max*10)):
        x.append(round(v0*math.cos(alfa_r)*t/10, 2))
        y.append(round(((v0*math.sin(alfa_r))*t/10 - (g*(t/10)**2)/2),2))
    return x,y 
x,y=hitac(200, 30)
x1,y1=hitac(220, 20)
# print(x)
# print(y)

# plt.plot(x,y)
# plt.xlabel('domet [m]')
# plt.ylabel('visina [m]')
# plt.title('Kosi Hitac')
''' Multiple plots in same grafic'''
chart, ax = plt.subplots()
chart.set_size_inches(10, 6)
ax.plot(x,y, label='200m/s, a=30°', color='orange')
ax.scatter(x1,y1, label='220m/s, a=20°', color='green', s=2)

ax.set_xlabel('domet [m]')
ax.set_ylabel('visina [m]')
ax.set_title('kosi hitac')
ax.legend()

plt.show()
    

  

