import pygame

class Ship:
    def __init__(self,ai_game):
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings

        self.ship_image=pygame.image.load('images/ship.bmp')

        self.ship_rect=self.ship_image.get_rect()
        self.ship_rect.midleft=self.screen_rect.midleft
        self.y=float(self.ship_rect.y)
        self.move_down=False
        self.move_up=False
    
    def blit_me(self):
        self.screen.blit(self.ship_image,self.ship_rect)
    
    def update(self):
        if self.move_up and self.ship_rect.top>=0:
            self.y-=self.settings.ship_speed
        if self.move_down and self.ship_rect.bottom<=self.settings.screen_height:
            self.y+=self.settings.ship_speed
        self.ship_rect.y=self.y
    
    def reset_ship(self):
        self.ship_rect.midleft=self.screen_rect.midleft
        self.y=float(self.ship_rect.y)