from turtle import *
state = {'turn':0}
def spinner():
    clear()
    angle = state['turn']/10
    right (angle)
    forward (100)
    dot (120, 'red')
    back (100)
    right (120)
    forward (100)
    dot (120, 'purple')
    back (100)
    right (120)
    forward (100)
    dot (120, 'orange')
    back (100)
    right (120)

def flip():
    state ['turn']+= 10
def animate():
    if (state['turn']> 0):
        state['turn']-= 1
    spinner()
    ontimer (animate, 20)
setup(420, 420, 370, 0)
tracer (False)
onkey(flip, 'space')
listen()
animate()
done ()