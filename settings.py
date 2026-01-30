class Settings:
    def __init__(self):
        self.screen_width,self.screen_height=(1200,800)
        self.screen_bg=(225,225,225)
        
        self.ship_speed=1.5
        
        self.chance_count=3
        
        self.width,self.height=(50,100)
        self.target_speed=2
        self.change_fleet_dir=1
        self.target_colour=(0,225,0)

        self.bullet_colour=(60,60,60)
        self.b_width,self.b_height=(40,2)
        self.bullet_speed=3
        self.allowed_bullets=3

        self.game_active=False