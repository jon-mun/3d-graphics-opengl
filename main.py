'''
Buatlah program untuk menggambar objek polyhedron (objek 3D yang permukaannya berbentuk Polygon) yang data objeknya terlampir, boleh menggunakan OpenGL atau library lainnya. Yang diupload program lengkap disertai beberapa output program dalam file format gambar atau dengan satu video.
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
        

class Polyhedron:
    
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        
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
                face = list(map(int, line.split()))
                faces.append(face)
            
            return rows, cols, vertices, faces

        except IOError:
            print(f"Error: Unable to read file '{filename}'.")

    def __str__(self):
        return f"Polyhedron(vertices={self.vertices}, faces={self.faces})"

poly = Polyhedron.from_text_file(filename="KUBUS4.txt")
print(poly)
