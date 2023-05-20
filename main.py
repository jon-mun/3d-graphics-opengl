'''
Buatlah program untuk menggambar objek polyhedron (objek 3D yang permukaannya berbentuk Polygon) yang data objeknya terlampir, boleh menggunakan OpenGL atau library lainnya. Yang diupload program lengkap disertai beberapa output program dalam file format gambar atau dengan satu video.
'''

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import sys

class Polyhedron:
    
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        
    def draw(self):        
        # draw faces
        glBegin(GL_QUADS)
        for face in self.faces:
            for vertex_index in face:
                vertex = self.vertices[vertex_index-1]
                glVertex3fv(vertex)
        glEnd()
        
    @staticmethod
    def from_text_file(filename):
        rows, cols, vertices, faces = Polyhedron.parse_text_file(filename)
        return Polyhedron(vertices, faces)

    @staticmethod
    def parse_text_file(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            
            lines = content.splitlines()
            rows, cols = map(int, lines[0].split())
            
            vertices = []
            for line in lines[1:rows+1]:
                vertex = list(map(float, line.split()))
                vertices.append(vertex)
            
            faces = []
            for line in lines[rows+1:]:
                # ex: 4 1 2 6 5, where the first line indicates the number of vertices in the face
                face = list(map(int, line.split()))
                face.pop(0) # remove first elemnt
                faces.append(face)
            
            return rows, cols, vertices, faces

        except IOError:
            print(f"Error: Unable to read file '{filename}'.")

    def __str__(self):
        return f"Polyhedron(\nvertices={self.vertices}, \nfaces={self.faces}), \nvertices={len(self.vertices)},\nfaces={len(self.faces)}\n)"

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -20)
    
    poly = Polyhedron.from_text_file(filename="KUBUS4.txt")
    # print(poly)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # draw
        poly.draw()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()