import subprocess
subprocess.call("./bin.sh", shell=True)
import glfw
from OpenGL.GL import *
import numpy as np
from math import sin, cos

# initializing glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized!")

# creating the window(width 720 * 480)
window = glfw.create_window(720, 480, "Naman", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# Query the actual framebuffer size so we can set the right viewport later
# -> glViewport(0, 0, framebuffer_size[0], framebuffer_size[1])
framebuffer_size = glfw.get_framebuffer_size(window)

# set window's position
glfw.set_window_pos(window, 400, 200)

# make the context current
glfw.make_context_current(window)

vertices = [-0.5, -0.5, 0.0,
             0.5, -0.5, 0.0,
             0.0,  0.5, 0.0]

colors = [1.0, 0.0, 0.0,
          0.0, 1.0, 0.0,
          0.0, 0.0, 1.0]

vertices = np.array(vertices, dtype=np.float32)
colors = np.array(colors, dtype=np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT, 0, vertices)

glEnableClientState(GL_COLOR_ARRAY)
glColorPointer(3, GL_FLOAT, 0, colors)
glClearColor(0, 0.1, 0.1, 1)#RGB Alpha(color)


# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()#use or program will crash
    glClear(GL_COLOR_BUFFER_BIT)
    ct = glfw.get_time()  # returns the elapsed time, since init was called

    glLoadIdentity()
    glScale(abs(sin(ct)), abs(sin(ct)), 1)
    glRotatef(sin(ct) * 50, 0, 0, 1)
    glTranslatef(sin(ct), cos(ct), 0)
    glDrawArrays(GL_TRIANGLES, 0, 3)
    glfw.swap_buffers(window)

# terminate glfw, free up allocated resources
glfw.terminate()
