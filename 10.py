class StateMachine:
    def __init__(self):
        self.state = 'A'

    def coat(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'C'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'F':
            self.state = 'D'
            return 9
        raise MealyError('coat')

    def rig(self):
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'D':
            self.state = 'E'
            return 5
        raise MealyError('rig')

    def mask(self):
        if self.state == 'C':
            self.state = 'F'
            return 3
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'D':
            self.state = 'G'
            return 6
        if self.state == 'G':
            self.state = 'H'
            return 10
        if self.state == 'H':
            self.state = 'B'
            return 11
        raise MealyError('mask')


class MealyError(Exception):
    pass


def raises(method, error):
    output = None
    try:
        output = method()
    except Exception as e:
        assert type(e) == error
    assert output is None


def main():
    return StateMachine()


def test():
    sm = StateMachine()
    assert sm.state == 'A'
    assert sm.coat() == 0
    assert sm.state == 'B'
    assert sm.coat() == 1
    assert sm.state == 'C'
    assert sm.coat() == 4
    assert sm.state == 'C'
    sm.state = 'E'
    raises(lambda: sm.coat(), MealyError)
    assert sm.state == 'F'
    assert sm.coat() == 9
    assert sm.state == 'D'
    sm.state = 'D'
    raises(lambda: sm.coat(), MealyError)
    assert sm.state == 'C'
    assert sm.rig() == 2
    assert sm.state == 'D'
    assert sm.rig() == 5
    assert sm.state == 'E'
    sm.state = 'D'
    raises(lambda: sm.rig(), MealyError)
    assert sm.state == 'C'
    assert sm.mask() == 3
    assert sm.state == 'F'
    assert sm.mask() == 8
    assert sm.state == 'G'
    assert sm.mask() == 6
    assert sm.state == 'G'
    assert sm.mask() == 10
    assert sm.state == 'H'
    assert sm.mask() == 11
    assert sm.state == 'B'
    raises(lambda: sm.mask(), MealyError)
