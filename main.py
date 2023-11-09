import pygame
import sys


SCREENWIDTH , SCREENHEIGHT = 1200 , 720#sets resolution to a constant 
FPS = 60 #sets frames per second to a constant
startImg = pygame.image.load('assets/start.jpg')
screen= pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("lurker")
class Game:#game class where all other classes are used
    def __init__(self):
        pygame.init()#gets all inbuilt pygame methods
       
        self.clock = pygame.time.Clock() 
       
    def run(self):
        while True:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          pygame.display.update()#changes screen on each iteration of loop
          self.clock.tick(FPS) # sets FPS to the constant
          screen.fill((255, 0, 0))#updates screen to fill in background
          startButton.draw()
          startButton.isClicked()
          pygame.display.flip()
          
          
             



    

class gameScenes:
  def __init__(self,display,gameState):
    self.display = display
    self.gameState= gameState
    
  """def setScene(self):
    if self.gamestate == "mainMenu":
  def buttons(self):
    mousePos = pygame.mouse.get_pos()
    if self"""
    

class button:
  def __init__(self,x,y,image):
    width = image.get_width() #is needed for scale of image if needed
    height = image.get_height()
    self.image = image  
    self.rect = self.image.get_rect() #adding outline box to image 
    self.rect.topleft = (x,y)#sets co-ordinates to topleft of box
    self.clicked = False #checks if a box has been clicked

  def draw(self):
    screen.blit(self.image,(self.rect.x,self.rect.y)) #draws button box 
  def isClicked(self):
    pos = pygame.mouse.get_pos() #checks mouse position to see if its on box
    if self.rect.collidepoint(pos):#checks if self.rect(the box) has mouse hovering over it
      if pygame.mouse.get_pressed()[0] ==1 and self.clicked == False:#checks if it has been clicked by left mouse button and extra validation to make sure clicks don't hold
        self.clicked = True
        print("button clicked")
      if pygame.mouse.get_pressed()[0] ==0:#when mouse isn't being clicked
        self.clicked = False #changes back to false to make the button usable again
   
        
    
   

startButton = button(500,100,startImg)
    

if __name__ == "__main__":
   
   
    game = Game()
    game.run()
   
   
    


"""class movement:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def move(self,x,y):
    self.x += x
    self.y += y
  def getX(self):
    return self.x
  def getY(self):
    return self.y
  def setX(self,x):
    self.x = x
  def setY(self,y):
    self.y = y"""