import pygame
import sys

class runner():
    pass

class Game():
    
    corredores = []
    
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((750, 315))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("image/background.png")
        
        self.runner = pygame.image.load("image/smallball.png")
        
    def competir(self):
        x = 0
        ganador = False
        while True:
            #comprobacion de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #Refrescar y renderizar la pantalla
            self.__screen.blit(self.background,(0,0))
            self.__screen.blit(self.runner,(x,170))
            pygame.display.flip()
            
            x += 3
            if x >= 250:
                ganador = True
        
        pygame.quit()
        sys.exit()
    


if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.competir()
      
       
