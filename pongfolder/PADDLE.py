import pygame


class PADDLE:
    """
    PADDLE class representing the player-controlled PADDLE.
    Handles PADDLE movement, drawing, and positioning.
    """

    def __init__(self, screen, GAME_CONFIG):
        """
        Initialize the PADDLE with default settings.

        Args:
            screen: The pygame display surface where the PADDLE will be drawn
        """

        self.config = GAME_CONFIG
        self.screen = screen
        self.paddleWidth: int = 20
        self.paddleHeight: int = 140
        self.paddleSpeed: float = 10.0 if self.config.difficulty['easy'] else 18.5 if self.config.difficulty[
            'medium'] else 23.8 \
            if self.config.difficulty['hard'] else 0.0
        self.paddleX: int = 50
        self.paddleY: float = float((self.screen.get_height() - self.paddleHeight) / 2)
        self.paddleRect: pygame.rect = pygame.Rect(self.paddleX, int(self.paddleY), self.paddleWidth,
                                                   self.paddleHeight)

    def MOVE(self, keys):
        """
        Move the PADDLE based on keyboard input.

        Args:
            keys: Sequence of boolean values representing keyboard state
        """

        self.paddleSpeed: int = 10 if self.config.difficulty['easy'] else 25 if self.config.difficulty[
            'medium'] else 50 \
            if self.config.difficulty['hard'] else 0

        if keys[pygame.K_UP]:
            self.paddleY = float(self.paddleY - self.paddleSpeed)

        if keys[pygame.K_DOWN]:
            self.paddleY = float(self.paddleY + self.paddleSpeed)

        self.paddleY = max(0.0, min(self.paddleY, float(self.screen.get_height() - self.paddleHeight)))
        self.paddleRect = pygame.Rect(self.paddleX, int(self.paddleY), self.paddleWidth, self.paddleHeight)

    def DRAW(self):
        """Draw the PADDLE on the screen."""

        pygame.draw.rect(self.screen, (255, 255, 255), self.paddleRect)


if __name__ == '__main__':
    from file_runner import runFile

    runFile('PONG.py')
