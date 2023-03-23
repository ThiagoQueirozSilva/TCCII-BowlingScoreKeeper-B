class Frame:
    def __init__(self, first_throw: int, second_throw: int) -> None:
        self.validateFrame(first_throw, second_throw)
        self.first_throw = first_throw
        self.second_throw = second_throw
        self.score = self.first_throw + self.second_throw

    def score(self) -> int:
        """ The score of a single frame """
        return self.score

    def is_strike(self) -> bool:
        """ Return whether the frame is a strike or not """
        if (self.first_throw == 10):
            return True
        return False

    def is_spare(self) -> bool:
        """ Return whether the frame is a spare or not """
        if(self.is_strike()):
            return False
        scoreCount = self.first_throw + self.second_throw
        if (scoreCount == 10):
            return True
        return False

    def is_last_frame(self, frameNumber: int) -> bool:
        """ Return whether the frame is a last frame of the game """
        if(frameNumber == 10):
            return True

    def bonus(self, addBonus : int):
        """ Bonus throw """
        self.score += addBonus

    def validateFrame(self,first : int, second : int):
        if (first == 10 and second > 0):
            raise Exception("Em um strike não deve jogar uma segunda vez na rodada")
        if (first < 0 or second < 0):
            raise Exception("Não é possível realizar uma pontuação negativa")
        if (first + second > 10):
            raise Exception("Não é possível derrubar mais de 10 pinos")
