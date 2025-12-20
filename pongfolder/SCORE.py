import pygame


class SCORE:
    """
    Score class handling game scoring and lives.
    """

    def __init__(self, GAME_CONFIG):
        """
        Initialize score tracking with default values.

        Args:
            GAME_CONFIG: GameConfig instance containing game settings
        """

        self.config = GAME_CONFIG
        self.score: int = 0
        self.lives: int = 10 if self.config.difficulty['easy'] else 5 if self.config.difficulty['medium'] else 1 if \
        self.config.difficulty['hard'] else 67
        self.lastTimeHit: int = 0

    def ADD_POINT(self):
        """Increment the score if enough time has passed since the last point."""

        currentTime = pygame.time.get_ticks()
        if currentTime - self.lastTimeHit > 500:
            self.score += 1
            self.lastTimeHit = currentTime

    def LOSE_LIFE(self):
        """
        Decrease lives count and check for game over.

        Returns:
            bool: True if no lives remain, False otherwise
        """

        currentTime = pygame.time.get_ticks()

        if currentTime - self.lastTimeHit > 10000:
            self.lives -= 1

        self.lastTimeHit = currentTime

        return self.lives <= 0


if __name__ == '__main__':
    from file_runner import runFile

    runFile('PONG.py')
