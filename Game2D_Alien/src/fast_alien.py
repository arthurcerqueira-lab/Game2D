from alien import Alien

class FastAlien(Alien):
    """Alien mais rapido"""
    
    def update(self) -> None:
        self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
        self.rect.x = self.x # Atualiza a posição do rect do alienígena com base na nova coordenada x