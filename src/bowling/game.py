from typing import List
from bowling.frame import Frame

class BowlingGame:
    def __init__ (self) -> None:
        self.frames = List[Frame]
        self.bonus = Frame
    frames = List[Frame]

    def add_frame(self, frame: Frame):
        """ Add a frame to the game """
        # To be implemented
        self.frames.append(Frame(frame.first_throw, frame.second_throw))

    def set_bonus(self, first_throw: int, second_throw: int):
        """ The the bonus throw """
        # To be implemented
        pass

    def score(self) -> int:
        """ Get the score from the game """
        # To be implemented
        pass

    def is_next_frame_bonus(self) -> bool:
        """ Get if the next frame is bonus """
        # To be implemented
        pass
