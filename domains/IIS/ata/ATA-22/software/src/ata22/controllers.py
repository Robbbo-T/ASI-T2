def clamp(x, lo, hi): return max(lo, min(hi, x))

class PID:
    def __init__(self, kp, ki, kd, lo=None, hi=None):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.i = 0.0
        self.lo, self.hi = lo, hi
        self.prev_e = 0.0

    def step(self, err, dt):
        self.i += err * dt * self.ki
        d = (err - self.prev_e) / dt if dt > 0 else 0.0
        self.prev_e = err
        u = self.kp * err + self.i + self.kd * d
        if self.lo is not None and self.hi is not None:
            u = clamp(u, self.lo, self.hi)
        return u