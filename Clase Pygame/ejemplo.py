import pygame
import sys

# Clase del juego
class Game:
    def __init__(self, width=800, height=600):
        pygame.init()  # Inicializa Pygame
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))  # Ventana
        pygame.display.set_caption("Mi Juego con Pygame")  # Título de la ventana
        self.clock = pygame.time.Clock()  # Reloj para controlar FPS
        self.running = True  # Estado del juego
        self.color = (0, 128, 255)  # Color de fondo (azul)

    def handle_events(self):
        """Maneja los eventos del juego."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Si se cierra la ventana
                self.running = False
            elif event.type == pygame.KEYDOWN:  # Si se presiona una tecla
                if event.key == pygame.K_q:  # Salir con 'q'
                    self.running = False

    def update(self):
        """Lógica del juego."""
        # Aquí puedes agregar la lógica de tu juego
        pass

    def draw(self):
        """Dibuja en la pantalla."""
        self.screen.fill(self.color)  # Rellena el fondo con un color
        pygame.draw.circle(self.screen, (255, 0, 0), (self.width // 2, self.height // 2), 50)  # Dibuja un círculo
        pygame.display.flip()  # Actualiza la pantalla

    def run(self):
        """Ciclo principal del juego."""
        while self.running:
            self.handle_events()  # Maneja eventos
            self.update()  # Actualiza la lógica
            self.draw()  # Dibuja en la pantalla
            self.clock.tick(60)  # Limita el juego a 60 FPS
        pygame.quit()  # Sale de Pygame

# Ejecuta el juego
if __name__ == "__main__":
    game = Game()  # Crea una instancia del juego
    game.run()  # Inicia el ciclo del juego
