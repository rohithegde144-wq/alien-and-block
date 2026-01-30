from pygame.sprite import Sprite
import pygame
class Rectangle(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen=ai_game.screen
        self.screen_rect=self.screen.get_rect()
        self.settings=ai_game.settings

        self.rect=pygame.Rect(0,0,self.settings.width,self.settings.height)
        self.rect.midright=self.screen_rect.midright
        self.y=float(self.rect.y)

    
    def update(self):
        if self.rect.bottom<=self.settings.screen_height or self.rect.top>=0:
            self.y+=self.settings.target_speed*self.settings.change_fleet_dir
            self.rect.y=self.y
    
    def draw_target(self):
        pygame.draw.rect(self.screen,self.settings.target_colour,self.rect)
    
    def reset_target(self):
        self.rect.midright=self.screen_rect.midright
        self.y=float(self.rect.y)