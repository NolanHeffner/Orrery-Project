from manim import *
from numpy import sqrt

config.background_color = "#111111"
config.frame_height = 450
config.frame_width = 800

class Orrery(Scene):
    def construct(self):
        Sun = Circle(radius=15)
        Sun.set_fill("#FFAA2F", opacity = 0.65)
        planet1 = Circle(radius=5)
        planet1.set_fill(LIGHT_BROWN, opacity = 0.7)
        planet2 = Circle(radius=5)
        planet2.set_fill(GREY_BROWN, opacity = 0.7)
        planet3 = Circle(radius=5)
        planet3.set_fill(GREEN, opacity = 0.7)
        planet4 = Circle(radius=5)
        planet4.set_fill("#E25923", opacity = 0.7)
        planet5 = Circle(radius=30)
        planet5.set_fill("#CFB182", opacity = 0.7)
        planet6 = Circle(radius=30)
        planet6.set_fill("#C8A773", opacity = 0.7)
        planet7 = Circle(radius=30)
        planet7.set_fill("#0CB9DB", opacity = 0.7)
        planet8 = Circle(radius=30)
        planet8.set_fill("#0B54C5", opacity = 0.7)
        
        self.add(Sun)
        self.add(planet1)
        self.add(planet2)
        self.add(planet3)
        self.add(planet4)
        self.add(planet5)
        self.add(planet6)
        self.add(planet7)
        self.add(planet8)
        
        Gmult = 6.673 * (10)
        mass = (1988435, 0.33, 4.87, 5.97, 0.642, 1898, 568, 86.8, 102)
        posX = [0, 57.9, 108.2, 149.6, 228, 778.5, 1432, 2867, 4515]
        posY = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        vX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        vY = [0, 47.4, 35, 29.8, 24.1, 13.1, 9.7, 6.8, 5.4]
        for i in range(9):
            vY[i] *= 86400 / 1000000
        stepsPerFrame = 1
        frame = 0
        while frame < 365:
            self.wait(0.1)
            for k in range(stepsPerFrame):
                aX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                aY = [0, 0, 0, 0, 0, 0, 0, 0, 0]
                for x in range(9):
                    x1 = posX[x]
                    y1 = posY[x]
                    for y in range(9):
                        x2 = posX[y]
                        y2 = posY[y]
                        r = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
                        if r > 0.1:
                            aX[x] += Gmult * mass[y] * (x2 - x1) / r**3
                            aY[x] += Gmult * mass[y] * (y2 - y1) / r**3
                for i in range(9):
                    h = 1 / stepsPerFrame
                    vX[i] += h * aX[i] / 86400
                    vY[i] += h * aY[i] / 86400
                    posX[i] += h * vX[i]
                    posY[i] += h * vY[i]
            planet1.move_to(np.array((posX[1], posY[1], 0.0)))
            planet2.move_to(np.array((posX[2], posY[2], 0.0)))
            planet3.move_to(np.array((posX[3], posY[3], 0.0)))
            planet4.move_to(np.array((posX[4], posY[4], 0.0)))
            planet5.move_to(np.array((posX[5], posY[5], 0.0)))
            planet6.move_to(np.array((posX[6], posY[6], 0.0)))
            planet7.move_to(np.array((posX[7], posY[7], 0.0)))
            planet8.move_to(np.array((posX[8], posY[8], 0.0)))
            frame += 1
            print("Step number: " + str(frame))