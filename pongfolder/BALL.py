import pygame, random


class BALL:
    """
    Ball class representing the game BALL.
    Handles BALL movement, collision detection, and drawing.
    """

    def __init__(self, GAME_CONFIG):
        """
        Initialize the BALL with default settings.

        Args:
            GAME_CONFIG: GameConfig instance containing game settings
        """

        self.config = GAME_CONFIG

        self.ballX: float = self.config.center[0]
        self.ballY: float = self.config.center[1]
        self.ballSpeed: float = 7.0 if self.config.difficulty['easy'] else 9.0 if self.config.difficulty[
            'medium'] else 11.0 if self.config.difficulty['hard'] else 7.0
        self.ballSpeedX: float = -self.ballSpeed + random.uniform(-5, 5)
        self.ballSpeedY: float = random.uniform(-self.ballSpeed, self.ballSpeed)
        self.ballSize: float = 10.88887 if self.config.difficulty['easy'] else 5.5555834 if self.config.difficulty[
            'medium'] else 2.5423 if self.config.difficulty['hard'] else 0.0
        self.ballRect: pygame.Rect = pygame.Rect(self.ballX, self.ballY, self.ballSize, self.ballSize)
        self.color = self.config.colors['BALL']

    def MOVE(self, paddle):
        """
        Update BALL position and handle collisions.

        Args:
            paddle: The player PADDLE for collision detection

        Returns:
            bool: True if BALL collides with PADDLE, False otherwise
        """

        self.ballX += self.ballSpeedX
        self.ballY += self.ballSpeedY
        self.ballRect.x = self.ballX
        self.ballRect.y = self.ballY
        self.ballSize: float = 10.88887 if self.config.difficulty['easy'] else 5.5555834 if self.config.difficulty[
            'medium'] else 2.5423 if self.config.difficulty['hard'] else 0.0
        self.ballSpeed: float = 7.0 if self.config.difficulty['easy'] else 9.0 if self.config.difficulty[
            'medium'] else 11.0 if self.config.difficulty['hard'] else 7.0

        if self.ballRect.colliderect(paddle.paddleRect):
            self.ballSpeedX *= -1

        if self.ballY <= 0 or self.ballY >= self.config.S_HEIGHT - self.ballSize:
            self.ballSpeedY *= -1

        if self.ballX >= self.config.S_WIDTH - self.ballSize:
            self.ballSpeedX *= -1

        if self.ballX < 0 + self.ballSize:
            return False

        return self.ballRect.colliderect(paddle.paddleRect)

    def RESET(self):
        """Reset the BALL to its initial position with new random velocity."""

        self.ballX = self.config.center[0]
        self.ballY = self.config.center[1]
        self.ballSpeedX = -self.ballSpeed
        self.ballSpeedY = random.uniform(-self.ballSpeed / 2, self.ballSpeed / 2)
        self.UPDATE_RECT()

    def UPDATE_RECT(self):
        """Update the BALL's rectangle position."""

        self.ballRect.x = self.ballX
        self.ballRect.y = self.ballY

    def DRAW(self):
        """Draw the BALL on the screen."""

        pygame.draw.rect(self.config.screen, self.color, self.ballRect)


if __name__ == '__main__':
    from file_runner import runFile

    runFile('PONG.py')
