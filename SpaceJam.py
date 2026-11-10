from direct.showbase.ShowBase import ShowBase
import sys, math, random
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses
import Player as playerClasses
from panda3d.core import CollisionTraverser, CollisionHandlerPusher, Vec3

class SpaceJam(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.accept("escape", self.quit)
        self.cTrav = CollisionTraverser()
        self.cTrav.traverse(self.render)
        self.pusher = CollisionHandlerPusher()
        self.SetupScene()

        self.SetCamera()
        self.Hero.SetKeyBindings()
        self.Hero.SetParticles()
        self.pusher.addCollider(self.Hero.collisionNode, self.Hero.modelNode)
        self.cTrav.addCollider(self.Hero.collisionNode, self.pusher)
        self.cTrav.showCollisions(self.render)

        fullCycle = 60
        halfCycle = 30
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCloudDefense(self.Planet1, nickName)
            self.DrawBaseballSeams(self.SpaceStation, nickName, j, fullCycle, 2)

        for i in range(halfCycle):
            spaceJamClasses.Drone.droneCount += 1
            nickName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawCircleXDefense(self.Planet2, nickName, i, halfCycle)
            self.DrawCircleYDefense(self.Planet3, nickName, i, halfCycle)
            self.DrawCircleZDefense(self.Planet4, nickName, i, halfCycle)

    def quit(self):
        sys.exit()

    def SetupScene(self):
        # Sets up Universe
        self.Universe = spaceJamClasses.Universe(self.loader, "./Assets/Universe/Universe.x", self.render, "Universe", "./Assets/Universe/universe.jpg", (0, 0, 0), 15000)
        # Sets up Planets
        self.Planet1 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet1", "./Assets/Planets/uranus.jpg", defensePaths.Cloud(8000), 350)
        self.Planet2 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet2", "./Assets/Planets/jupiter.jpg", defensePaths.Cloud(8000), 350)
        self.Planet3 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet3", "./Assets/Planets/mars.jpg", defensePaths.Cloud(8000), 350)
        self.Planet4 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet4", "./Assets/Planets/neptune.jpg", defensePaths.Cloud(8000), 350)
        self.Planet5 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet5", "./Assets/Planets/mercury.jpg", defensePaths.Cloud(8000), 350)
        self.Planet6 = spaceJamClasses.Planet(self.loader, "./Assets/Planets/protoPlanet.x", self.render, "Planet6", "./Assets/Planets/venus.jpg", defensePaths.Cloud(8000), 350)
        # Sets up SpaceStation
        self.SpaceStation = spaceJamClasses.SpaceStation(self.loader, "./Assets/SpaceStation/spaceStation.egg", self.render, "Space Station", "./Assets/SpaceStation/SpaceStation1_Dif2.png", defensePaths.Cloud(8000), 40)
        # Sets up Player's Ship
        self.Hero = playerClasses.SpaceShip(self.loader, self.taskMgr, self.accept, "./Assets/Spaceships/Dumbledore.egg", self.render, "Hero", "./Assets/Spaceships/spacejet_C.png", defensePaths.Cloud(8000), 25, self.cTrav)

    def DrawBaseballSeams(self, centralObject, droneName, step, numSeams, radius = 1):
        unitVec = defensePaths.BaseballSeams(step, numSeams, B = 0.4)
        unitVec.normalize()
        position = unitVec * radius * 250 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 7)

    def DrawCloudDefense(self, centralObject, droneName):
        unitVec = defensePaths.Cloud()
        unitVec.normalize()
        position = unitVec * 500 + centralObject.modelNode.getPos()
        spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 7)

    def DrawCircleXDefense(self, centralObject, droneName, step, amount):
            unitVec = defensePaths.CircleX(step, amount)
            unitVec.normalize()
            position = unitVec * 500 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 7)
    
    def DrawCircleYDefense(self, centralObject, droneName, step, amount):
            unitVec = defensePaths.CircleY(step, amount)
            unitVec.normalize()
            position = unitVec * 500 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 7)
    
    def DrawCircleZDefense(self, centralObject, droneName, step, amount):
            unitVec = defensePaths.CircleZ(step, amount)
            unitVec.normalize()
            position = unitVec * 500 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "./Assets/DroneDefender/octotoad1_auv.png", position, 7)

    def SetCamera(self):
            self.disableMouse()
            self.camera.reparentTo(self.Hero.modelNode)
            self.camera.setFluidPos(0, 1, 0)

game = SpaceJam()
game.run()