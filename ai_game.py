import pygame
import sys
from settings import Settings
from ship import Ship
from rectangle import Rectangle
from bullets import Bullets
from game_stats import GameStats
from button import Button
from time import sleep
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.screen_rect=self.screen.get_rect()
        self.ship=Ship(self)
        self.rectangle=Rectangle(self)
        self.bullet=Bullets(self)
        self.bullets=pygame.sprite.Group()
        self.rectangle_group=pygame.sprite.Group()
        self.rectangle_group.add(self.rectangle)
        self.stats=GameStats(self)
        self.button=Button(self,"Play")

    def run_game(self):
        while True:
                self._check_events()
                if self.stats.game_active:
                    self._update_sprites_()
                    self._check_hit()
                self._reset_game()
                self._draw_sprites()

    def _check_events(self):
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._key_down_events(event)
                elif event.type==pygame.KEYUP:
                    self._key_up_events(event)
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    mouse_pos=pygame.mouse.get_pos()
                    self._check_play_button(mouse_pos)
                

    def _key_down_events(self,event):
        if event.key==pygame.K_DOWN:
            self.ship.move_down=True
        elif event.key==pygame.K_UP:
            self.ship.move_up=True
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()
        elif event.key==pygame.K_p:
            self._key_start()
    
    def _check_play_button(self,mouse_pos):
        if self.button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.stats.game_active=True
            self._reset_stats_ship_target()
            pygame.mouse.set_visible(False)
    
    def _key_up_events(self,event):
        if event.key==pygame.K_DOWN:
            self.ship.move_down=False
        if event.key==pygame.K_UP:
            self.ship.move_up=False
    
    def _check_hit(self):
        if self.rectangle.rect.bottom>=self.settings.screen_height or self.rectangle.rect.top<=0:
            self.settings.change_fleet_dir*=-1
    
    def _fire_bullet(self):
        new_bullet=Bullets(self)
        if len(self.bullets)<self.settings.allowed_bullets:
            self.bullets.add(new_bullet)  

    def _update_sprites_(self):
        self.ship.update()
        self.rectangle.update()
        self.bullets.update()
        collision=pygame.sprite.groupcollide(self.bullets,self.rectangle_group,True,False)
        if collision:
            pass
        self.remove_bullets()
    
    def _key_start(self):
        self.stats.game_active=True
        self._reset_stats_ship_target()
        pygame.mouse.set_visible(False)

    def remove_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.x>=self.settings.screen_width:
                self.bullets.remove(bullet)
                self.stats.bullet_count+=1
        
    def _draw_sprites(self):
        self.screen.fill(self.settings.screen_bg)
        self.rectangle.draw_target()
        self.ship.blit_me()
        self._draw_bullets()
        if not self.stats.game_active:
            self.button.draw_button()
        pygame.display.flip()
    
    def _draw_bullets(self):
        for bullets in self.bullets.sprites():
            bullets.draw_bullet()

    def _reset_game(self):
        if self.stats.bullet_count>=self.settings.allowed_bullets:
            self.stats.game_active=False
            pygame.mouse.set_visible(True) 
            sleep(0.5)
    
    def _reset_stats_ship_target(self):
        self.stats.reset_stats()
        self.ship.reset_ship()
        self.rectangle.reset_target()             

if "__main__"==__name__:
    ai_game=AlienInvasion()
    ai_game.run_game()