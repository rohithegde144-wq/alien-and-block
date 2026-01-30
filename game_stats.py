class GameStats:
    def __init__(self,ai_game):
        self.settings=ai_game.settings
        self.reset_stats()
        self.game_active=False
        self.bullet_count=0
        self.collision_count=0
    
    def reset_stats(self):
        self.attempts=self.settings.chance_count
        self.bullet_count=0
        self.collision_count=0
        

        