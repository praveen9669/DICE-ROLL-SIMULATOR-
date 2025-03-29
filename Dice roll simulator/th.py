import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

# Initialize Pygame and OpenGL
pygame.init()
width, height = 600, 600
screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
gluPerspective(45, (width / height), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

def load_texture(image_path):
    texture_surface = pygame.image.load(image_path)
    texture_data = pygame.image.tostring(texture_surface, "RGBA", True)
    width, height = texture_surface.get_size()
    
    tex_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, tex_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, texture_data)
    return tex_id

# Load dice textures
dice_faces = [
    load_texture("Images/1.png"), load_texture("Images/2.png"), load_texture("Images/3.png"),
    load_texture("Images/4.png"), load_texture("Images/5.png"), load_texture("Images/6.png")
]

def draw_dice():
    glEnable(GL_TEXTURE_2D)

    faces = [
        (dice_faces[0], [(-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]),  # Front (1)
        (dice_faces[5], [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1)]),  # Back (6)
        (dice_faces[2], [(-1, -1, -1), (-1, -1, 1), (-1, 1, 1), (-1, 1, -1)]),  # Left (3)
        (dice_faces[3], [(1, -1, -1), (1, -1, 1), (1, 1, 1), (1, 1, -1)]),  # Right (4)
        (dice_faces[1], [(-1, 1, -1), (1, 1, -1), (1, 1, 1), (-1, 1, 1)]),  # Top (2)
        (dice_faces[4], [(-1, -1, -1), (1, -1, -1), (1, -1, 1), (-1, -1, 1)])  # Bottom (5)
    ]

    for texture, vertices in faces:
        glBindTexture(GL_TEXTURE_2D, texture)  # Move texture binding outside glBegin/glEnd
        glBegin(GL_QUADS)
        glTexCoord2f(0, 0); glVertex3f(*vertices[0])
        glTexCoord2f(1, 0); glVertex3f(*vertices[1])
        glTexCoord2f(1, 1); glVertex3f(*vertices[2])
        glTexCoord2f(0, 1); glVertex3f(*vertices[3])
        glEnd()  # Ensure glEnd() only contains valid OpenGL commands

    glDisable(GL_TEXTURE_2D)  # Disable texturing after drawing


# Animation loop
rolling = True
x_rot, y_rot = 0, 0
final_x, final_y = random.randint(0, 360), random.randint(0, 360)
while rolling:
    for event in pygame.event.get():
        if event.type == QUIT:
            rolling = False
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glRotatef(x_rot, 1, 0, 0)
    glRotatef(y_rot, 0, 1, 0)
    draw_dice()
    glPopMatrix()
    pygame.display.flip()
    pygame.time.wait(30)
    
    if abs(x_rot - final_x) < 2 and abs(y_rot - final_y) < 2:
        rolling = False
    else:
        x_rot += (final_x - x_rot) * 0.1
        y_rot += (final_y - y_rot) * 0.1

pygame.quit()
