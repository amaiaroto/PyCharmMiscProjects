import sys

import pygame, time

from PADDLE import PADDLE
from BALL import BALL
from SCORE import SCORE
from GAME_CONFIG import GameConfig


class GAME:
    """
    Main game class handling game loop and state.
    """

    def __init__(self):
        """Initialize the game state and objects."""

        self.config = GameConfig()
        self.PADDLE = PADDLE(self.config.screen, self.config)
        self.BALL = BALL(self.config)
        self.SCORE = SCORE(self.config)
        self.gameOver = False
        self.clock = pygame.time.Clock()
        self.directionSet = False

        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)

    def UPDATE(self, keys):
        """
        Update game state based on input and game logic.

        Args:
            keys: Keyboard input state
        """

        if not self.gameOver:
            self.PADDLE.MOVE(keys)

            if self.BALL.MOVE(self.PADDLE):
                self.SCORE.ADD_POINT()

            if self.BALL.ballX + self.BALL.ballSize < 0:
                if self.SCORE.LOSE_LIFE():
                    self.gameOver = True

                self.BALL.RESET()

    def DRAW(self):
        """Draw the current game state to the screen."""

        self.config.screen.fill(self.config.colors['BACKGROUND'])

        self.PADDLE.DRAW()
        self.BALL.DRAW()

        scoreText = self.config.font.render(f'Score: {self.SCORE.score}', True, self.config.colors['TEXT SCORE'])
        livesText = self.config.font.render(f'Lives: {self.SCORE.lives}', True, self.config.colors['TEXT LIVES'])

        self.config.screen.blit(scoreText, (20, 20))
        self.config.screen.blit(livesText, (20, 60))

        if self.gameOver:
            self.config.screen.fill(self.config.colors['BACKGROUND'])
            self.config.drawGameOver()

        pygame.display.flip()

    def RUN(self):
        """Main game loop."""

        pygame.display.set_caption('Pong')

        sc = pygame.display.set_mode((1000, 800), pygame.FULLSCREEN)
        fon = pygame.font.Font(None, 72)

        tex = fon.render('Start', True, (0, 255, 0))
        texRRR = tex.get_rect(center=(sc.get_width() / 2, sc.get_height() / 2.5))
        sc.blit(tex, texRRR)

        pygame.display.flip()

        time.sleep(1.57)
        sc.fill((0, 0, 0))

        pygame.display.flip()

        RUNNING = True
        while RUNNING:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUNNING = False

            if self.gameOver:
                time.sleep(1)
                break  # Go back to the menu after game over

            if self.SCORE.score >= 50:
                self.config.difficulty['hard'] = True
                self.config.difficulty['medium'] = False
                self.config.difficulty['easy'] = False

            elif self.SCORE.score >= 10:
                self.config.difficulty['hard'] = False
                self.config.difficulty['medium'] = True
                self.config.difficulty['easy'] = False

            else:
                self.config.difficulty['hard'] = False
                self.config.difficulty['medium'] = False
                self.config.difficulty['easy'] = True

            keys = pygame.key.get_pressed()
            self.UPDATE(keys)
            self.DRAW()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    with __import__('code_holder') as mod:
        Code = mod.Code

    PONG: Code = Code('PONG.py')
    PONG.run()
