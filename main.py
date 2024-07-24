import pygame
pygame.init()
import math


HEIGHT = 800
WIDTH = 800

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitysim")


class Planet:
    
    AU = (149.6e6 * 1000)
    G = 6.67428e-11
    SCALE = 250/AU #1AU = 100px
    TIMESTEP = 3600*24 #1 day
    
    def __init__(self, x, y, radius, color, mass):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.mass=mass
        
        self.sun = False
        self.distance_to_sun = 0
        self.orbit = []
        
        self.x_vel=0
        self.y_vel=0
        
    def draw(self, win):
        x = self.x*self.SCALE + WIDTH/2
        y = self.y*self.SCALE + HEIGHT/2
        pygame.draw.circle(win, self.color, (x,y), self.radius)
        
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x=other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if other.sun:
            self.distance_to_sun = distance

        
        force = self.G * self.mass * other.mass / distance**2
        
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta)*force
        force_y = math.sin(theta)*force
        return force_x, force_y
    
    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy
            
        self.x_vel += total_fx / self.mass*self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP
        
        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
        
def main():
    run = True
    clock = pygame.time.Clock()
    
    
    sun = Planet(0,0, 30, (255,255,0), 1.98892*10**30)
    sun.sun=True
    
    earth = Planet(-1*Planet.AU,0,16,(100,149,237),5.9742*10**24)
    earth.y_vel = 29.783 * 1000
    
    planets = [sun, earth]
    
    while run:
        clock.tick(60)
        pygame.display.update()
        win.fill((0,0,0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        for planet in planets:
            planet.update_position(planets)
            planet.draw(win)
            
        pygame.display.update()
                
    pygame.quit()
    
main()
            
    
    

