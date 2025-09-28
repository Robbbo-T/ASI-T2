def clamp(x, lo, hi): return max(lo, min(hi, x))

class PID:
    def __init__(self, kp, ki, kd, lo=None, hi=None):
        self.kp, self.ki, self.kd = kp, ki, kd
        self.i = 0.0
        self.lo, self.hi = lo, hi
        self.prev_e = 0.0

    def step(self, err, dt):
        # Compute derivative
        d = (err - self.prev_e) / dt if dt > 0 else 0.0
        # Predict next integral
        i_next = self.i + err * dt * self.ki
        # Compute unclamped output
        u_unclamped = self.kp * err + i_next + self.kd * d
        # Clamp output if limits are set
        if self.lo is not None and self.hi is not None:
            u = clamp(u_unclamped, self.lo, self.hi)
        else:
            u = u_unclamped
        # Anti-windup: Only integrate if not saturated, or if error is driving output back toward unsaturated region
        if (u == u_unclamped) or \
           (u == self.lo and err > 0) or \
           (u == self.hi and err < 0):
            self.i = i_next
        # Update previous error
        self.prev_e = err
        return u