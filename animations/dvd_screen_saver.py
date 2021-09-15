class DVDScreenSaver:
    def __init__(self,
                 size: tuple,
                 clip_size: tuple,
                 start_position: int = 0,
                 speed: int = 5):
        self._W, self._H = size
        self._w, self._h = clip_size
        self._start_position = start_position
        self._xV = speed
        self._yV = speed
        self._x = start_position
        self._y = start_position

    def calculate_position(self, t: int) -> tuple:
        """Returns x, y position given the time

        :type t: int
        :param t: current time
        """
        self._x += self._xV
        self._y += self._yV
        self.detect_collision()
        return self._x, self._y

    def detect_collision(self):
        """Detects collision with the outer walls and prevents it. """
        if (self._y + self._h) == self._H:
            self._yV = -self._yV
        if (self._x + self._w) == self._W:
            self._xV = -self._xV
        if self._x == 0:
            self._xV = -self._xV
        if self._y == 0:
            self._yV = -self._yV
