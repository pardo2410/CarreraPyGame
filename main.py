import pygame
import sys
import random

class runner():
    pass

class Game():
    
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((1755, 315))
        pygame.display.set_caption("Gran Carrera")
        self.background = pygame.image.load("image/background.png")        
      
        self.runner = pygame.image.load("image/smallball.png")
        self.runner2 = pygame.image.load("image/smallball2.png")
        
    def competir(self):
        x = 0
        y= 0
        ganador = False
        while True:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #Refrescar y renderizar la pantalla
            self.__screen.blit(self.background,(0,0))
            self.__screen.blit(self.runner,(x,90))
            self.__screen.blit(self.runner2,(y,170))
            pygame.display.flip()
            
            x += random.randint(1,10)
            y += random.randint(1,10)
            if x >= 1700 or y >= 1700:
                ganador = True
                if x>y:
                    print('El ganador de la carrera es {}'.format('Runner 1'))
                else:
                    print('El ganador de la carrera es {}'.format('Runner 2'))
                break                   
                                
                
            
        
        pygame.quit()
        sys.exit()
    


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
      
       
