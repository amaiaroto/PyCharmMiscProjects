import pygame

from SCORE import SCORE


class GameConfig:
    """
    Configuration and constants for the game.
    Handles display settings, colors, and difficulty settings.
    """

    def __init__(self):
        """
        Initialize game configuration with default settings.
        Sets up display, fonts, colors, and difficulty levels.
        """

        # Display
        self.screen: pygame.Surface = pygame.display.set_mode((2000, 1200), pygame.FULLSCREEN)
        self.S_WIDTH: float = self.screen.get_width()
        self.S_HEIGHT: float = self.screen.get_height()
        self.center: tuple[float, float] = (self.S_WIDTH / 2, self.S_HEIGHT / 2)
        self.SCORE = SCORE(GameConfig)

        # Fonts
        self.font: pygame.font.Font = pygame.font.Font(None, 36)
        self.bigFont: pygame.font.Font = pygame.font.Font(None, 150)

        self.WHITE: tuple[int, int, int] = (255, 255, 255)
        self.BLACK: tuple[int, int, int] = (0, 0, 0)
        self.RED: tuple[int, int, int] = (255, 0, 0)
        self.BLUE: tuple[int, int, int] = (0, 0, 255)
        self.GREEN: tuple[int, int, int] = (0, 255, 0)

        # Colors
        self.colors: dict[str, tuple[int, int, int]] = {
            'PADDLE': self.WHITE,
            'BALL': self.WHITE,
            'TEXT SCORE': self.BLUE,
            'TEXT LIVES': self.GREEN,
            'GAME OVER TEXT': self.RED,
            'BACKGROUND': self.BLACK
        }

        # Difficulty settings
        self.difficulty: dict[str, bool] = {
            'easy': False,
            'medium': True,
            'hard': False
        }

    def drawGameStats(self):
        """Draw the game statistics (score and lives) on the screen."""

        # Score
        scoreText = self.font.render(f'Score: {self.SCORE.score}', True, self.colors['TEXT SCORE'])
        self.screen.blit(scoreText, (20, 20))

        # Lives
        livesText = self.font.render(f'Lives: {self.SCORE.lives}', True, self.colors['TEXT LIVES'])
        self.screen.blit(livesText, (20, 60))

    def drawGameOver(self):
        """Draw the game over the screen with centered text."""

        gameOverText1 = self.bigFont.render('GAME', True, self.colors['GAME OVER TEXT'])
        gameOverText2 = self.bigFont.render('OVER', True, self.colors['GAME OVER TEXT'])
        textRect1: pygame.Rect = gameOverText1.get_rect(center=(self.center[0] - 10, self.center[1] - 50))
        textRect2: pygame.Rect = gameOverText2.get_rect(
            center=(self.center[0] - 10, (self.center[1] + textRect1.height - 35)))
        self.screen.blit(gameOverText1, textRect1)
        self.screen.blit(gameOverText2, textRect2)


if __name__ == '__main__':
    exec(open('PONG.py', 'r').read(), globals())
