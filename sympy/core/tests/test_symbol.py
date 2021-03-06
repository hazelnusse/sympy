from sympy import (Symbol, Wild, GreaterThan, LessThan, StrictGreaterThan,
    StrictLessThan, pi, I, Rational, sympify, symbols, Dummy, Function, flatten
)

from sympy.utilities.pytest import raises, XFAIL
from sympy.utilities.exceptions import SymPyDeprecationWarning


def test_Symbol():
    a = Symbol("a")
    x1 = Symbol("x")
    x2 = Symbol("x")
    xdummy1 = Dummy("x")
    xdummy2 = Dummy("x")

    assert a != x1
    assert a != x2
    assert x1 == x2
    assert x1 != xdummy1
    assert xdummy1 != xdummy2

    assert Symbol("x") == Symbol("x")
    assert Dummy("x") != Dummy("x")
    d = symbols('d', cls=Dummy)
    assert isinstance(d, Dummy)
    c, d = symbols('c,d', cls=Dummy)
    assert isinstance(c, Dummy)
    assert isinstance(d, Dummy)
    raises(TypeError, lambda: Symbol())


def test_Dummy():
    assert Dummy() != Dummy()
    Dummy._count = 0
    d1 = Dummy()
    Dummy._count = 0
    assert d1 == Dummy()


def test_as_dummy():
    x = Symbol('x')
    x1 = x.as_dummy()
    assert x1 != x
    assert x1 != x.as_dummy()

    x = Symbol('x', commutative=False)
    x1 = x.as_dummy()
    assert x1 != x
    assert x1.is_commutative is False


def test_lt_gt():
    from sympy import sympify as S
    x, y = Symbol('x'), Symbol('y')

    assert (x >= y) == GreaterThan(x, y)
    assert (x >= 0) == GreaterThan(x, 0)
    assert (x <= y) == LessThan(x, y)
    assert (x <= 0) == LessThan(x, 0)

    assert (0 <= x) == GreaterThan(x, 0)
    assert (0 >= x) == LessThan(x, 0)
    assert (S(0) >= x) == GreaterThan(0, x)
    assert (S(0) <= x) == LessThan(0, x)

    assert (x > y) == StrictGreaterThan(x, y)
    assert (x > 0) == StrictGreaterThan(x, 0)
    assert (x < y) == StrictLessThan(x, y)
    assert (x < 0) == StrictLessThan(x, 0)

    assert (0 < x) == StrictGreaterThan(x, 0)
    assert (0 > x) == StrictLessThan(x, 0)
    assert (S(0) > x) == StrictGreaterThan(0, x)
    assert (S(0) < x) == StrictLessThan(0, x)

    e = x**2 + 4*x + 1
    assert (e >= 0) == GreaterThan(e, 0)
    assert (0 <= e) == GreaterThan(e, 0)
    assert (e > 0) == StrictGreaterThan(e, 0)
    assert (0 < e) == StrictGreaterThan(e, 0)

    assert (e <= 0) == LessThan(e, 0)
    assert (0 >= e) == LessThan(e, 0)
    assert (e < 0) == StrictLessThan(e, 0)
    assert (0 > e) == StrictLessThan(e, 0)

    assert (S(0) >= e) == GreaterThan(0, e)
    assert (S(0) <= e) == LessThan(0, e)
    assert (S(0) < e) == StrictLessThan(0, e)
    assert (S(0) > e) == StrictGreaterThan(0, e)


def test_no_len():
    # there should be no len for numbers
    x = Symbol('x')
    raises(TypeError, lambda: len(x))


def test_ineq_unequal():
    S = sympify

    x, y, z = symbols('x,y,z')

    e = (
        S(-1) >= x, S(-1) >= y, S(-1) >= z,
        S(-1) > x, S(-1) > y, S(-1) > z,
        S(-1) <= x, S(-1) <= y, S(-1) <= z,
        S(-1) < x, S(-1) < y, S(-1) < z,
        S(0) >= x, S(0) >= y, S(0) >= z,
        S(0) > x, S(0) > y, S(0) > z,
        S(0) <= x, S(0) <= y, S(0) <= z,
        S(0) < x, S(0) < y, S(0) < z,
        S('3/7') >= x, S('3/7') >= y, S('3/7') >= z,
        S('3/7') > x, S('3/7') > y, S('3/7') > z,
        S('3/7') <= x, S('3/7') <= y, S('3/7') <= z,
        S('3/7') < x, S('3/7') < y, S('3/7') < z,
        S(1.5) >= x, S(1.5) >= y, S(1.5) >= z,
        S(1.5) > x, S(1.5) > y, S(1.5) > z,
        S(1.5) <= x, S(1.5) <= y, S(1.5) <= z,
        S(1.5) < x, S(1.5) < y, S(1.5) < z,
        S(2) >= x, S(2) >= y, S(2) >= z,
        S(2) > x, S(2) > y, S(2) > z,
        S(2) <= x, S(2) <= y, S(2) <= z,
        S(2) < x, S(2) < y, S(2) < z,
        x >= -1, y >= -1, z >= -1,
        x > -1, y > -1, z > -1,
        x <= -1, y <= -1, z <= -1,
        x < -1, y < -1, z < -1,
        x >= 0, y >= 0, z >= 0,
        x > 0, y > 0, z > 0,
        x <= 0, y <= 0, z <= 0,
        x < 0, y < 0, z < 0,
        x >= 1.5, y >= 1.5, z >= 1.5,
        x > 1.5, y > 1.5, z > 1.5,
        x <= 1.5, y <= 1.5, z <= 1.5,
        x < 1.5, y < 1.5, z < 1.5,
        x >= 2, y >= 2, z >= 2,
        x > 2, y > 2, z > 2,
        x <= 2, y <= 2, z <= 2,
        x < 2, y < 2, z < 2,

        x >= y, x >= z, y >= x, y >= z, z >= x, z >= y,
        x > y, x > z, y > x, y > z, z > x, z > y,
        x <= y, x <= z, y <= x, y <= z, z <= x, z <= y,
        x < y, x < z, y < x, y < z, z < x, z < y,

        x - pi >= y + z, y - pi >= x + z, z - pi >= x + y,
        x - pi > y + z, y - pi > x + z, z - pi > x + y,
        x - pi <= y + z, y - pi <= x + z, z - pi <= x + y,
        x - pi < y + z, y - pi < x + z, z - pi < x + y,
        True, False
    )

    left_e = e[:-1]
    for i, e1 in enumerate( left_e ):
        for e2 in e[i + 1:]:
            assert e1 != e2


def test_Wild_properties():
    # these tests only include Atoms
    x = Symbol("x")
    y = Symbol("y")
    p = Symbol("p", positive=True)
    k = Symbol("k", integer=True)
    n = Symbol("n", integer=True, positive=True)

    given_patterns = [ x, y, p, k, -k, n, -n, sympify(-3), sympify(3),
                       pi, Rational(3, 2), I ]

    integerp = lambda k: k.is_integer
    positivep = lambda k: k.is_positive
    symbolp = lambda k: k.is_Symbol
    realp = lambda k: k.is_real

    S = Wild("S", properties=[symbolp])
    R = Wild("R", properties=[realp])
    Y = Wild("Y", exclude=[x, p, k, n])
    P = Wild("P", properties=[positivep])
    K = Wild("K", properties=[integerp])
    N = Wild("N", properties=[positivep, integerp])

    given_wildcards = [ S, R, Y, P, K, N ]

    goodmatch = {
        S: (x, y, p, k, n),
        R: (p, k, -k, n, -n, -3, 3, pi, Rational(3, 2)),
        Y: (y, -3, 3, pi, Rational(3, 2), I ),
        P: (p, n, 3, pi, Rational(3, 2)),
        K: (k, -k, n, -n, -3, 3),
        N: (n, 3)}

    for A in given_wildcards:
        for pat in given_patterns:
            d = pat.match(A)
            if pat in goodmatch[A]:
                assert d[A] in goodmatch[A]
            else:
                assert d is None


@XFAIL
def test_symbols_each_char():
    # XXX: Because of the way the warnings filters work, this will fail if it's
    # run more than once in the same session.  See issue 2492.
    import warnings
    # each_char is deprecated and emits a warning.

    w = Symbol('w')
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')

    # First, test the warning
    warnings.filterwarnings("error")
    raises(SymPyDeprecationWarning, lambda: symbols('xyz', each_char=True))
    raises(SymPyDeprecationWarning, lambda: symbols('xyz', each_char=False))
    # now test the actual output
    warnings.filterwarnings("ignore")
    assert symbols(['wx', 'yz'], each_char=True) == [(w, x), (y, z)]
    assert all(w.is_Function for w in flatten(
        symbols(['wx', 'yz'], each_char=True, cls=Function)))
    assert symbols('xyz', each_char=True) == (x, y, z)
    assert symbols('x,', each_char=True) == (x,)
    assert symbols('x y z', each_char=True) == symbols(
        'x,y,z', each_char=True) == (x, y, z)
    assert symbols('xyz', each_char=False) == Symbol('xyz')
    a, b = symbols('x y', each_char=False, real=True)
    assert a.is_real and b.is_real
    assert 'each_char' not in a.assumptions0

    assert symbols('x0:0', each_char=False) == ()
    assert symbols('x0:1', each_char=False) == (Symbol('x0'),)
    assert symbols(
        'x0:3', each_char=False) == (Symbol('x0'), Symbol('x1'), Symbol('x2'))
    assert symbols('x:0', each_char=False) == ()
    assert symbols('x:1', each_char=False) == (Symbol('x0'),)
    assert symbols(
        'x:3', each_char=False) == (Symbol('x0'), Symbol('x1'), Symbol('x2'))
    assert symbols('x1:1', each_char=False) == ()
    assert symbols('x1:2', each_char=False) == (Symbol('x1'),)
    assert symbols('x1:3', each_char=False) == (Symbol('x1'), Symbol('x2'))

    # Keep testing reasonably thread safe, so reset the warning
    warnings.filterwarnings("default", "The each_char option to symbols\(\) and var\(\) is "
        "deprecated.  Separate symbol names by spaces or commas instead.")
    # Note, in Python 2.6+, this can be done more nicely using the
    # warnings.catch_warnings context manager.
    # See http://docs.python.org/library/warnings#testing-warnings.


def test_symbols():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')

    assert symbols('x') == x
    assert symbols('x ') == x
    assert symbols(' x ') == x
    assert symbols('x,') == (x,)
    assert symbols('x, ') == (x,)
    assert symbols('x ,') == (x,)

    assert symbols('x , y') == (x, y)

    assert symbols('x,y,z') == (x, y, z)
    assert symbols('x y z') == (x, y, z)

    assert symbols('x,y,z,') == (x, y, z)
    assert symbols('x y z ') == (x, y, z)

    xyz = Symbol('xyz')
    abc = Symbol('abc')

    assert symbols('xyz') == xyz
    assert symbols('xyz,') == (xyz,)
    assert symbols('xyz,abc') == (xyz, abc)

    assert symbols(('xyz',)) == (xyz,)
    assert symbols(('xyz,',)) == ((xyz,),)
    assert symbols(('x,y,z,',)) == ((x, y, z),)
    assert symbols(('xyz', 'abc')) == (xyz, abc)
    assert symbols(('xyz,abc',)) == ((xyz, abc),)
    assert symbols(('xyz,abc', 'x,y,z')) == ((xyz, abc), (x, y, z))

    assert symbols(('x', 'y', 'z')) == (x, y, z)
    assert symbols(['x', 'y', 'z']) == [x, y, z]
    assert symbols(set(['x', 'y', 'z'])) == set([x, y, z])

    raises(ValueError, lambda: symbols(''))
    raises(ValueError, lambda: symbols(','))
    raises(ValueError, lambda: symbols('x,,y,,z'))
    raises(ValueError, lambda: symbols(('x', '', 'y', '', 'z')))

    a, b = symbols('x,y', real=True)
    assert a.is_real and b.is_real

    x0 = Symbol('x0')
    x1 = Symbol('x1')
    x2 = Symbol('x2')

    y0 = Symbol('y0')
    y1 = Symbol('y1')

    assert symbols('x0:0') == ()
    assert symbols('x0:1') == (x0,)
    assert symbols('x0:2') == (x0, x1)
    assert symbols('x0:3') == (x0, x1, x2)

    assert symbols('x:0') == ()
    assert symbols('x:1') == (x0,)
    assert symbols('x:2') == (x0, x1)
    assert symbols('x:3') == (x0, x1, x2)

    assert symbols('x1:1') == ()
    assert symbols('x1:2') == (x1,)
    assert symbols('x1:3') == (x1, x2)

    assert symbols('x1:3,x,y,z') == (x1, x2, x, y, z)

    assert symbols('x:3,y:2') == (x0, x1, x2, y0, y1)
    assert symbols(('x:3', 'y:2')) == ((x0, x1, x2), (y0, y1))

    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    d = Symbol('d')

    assert symbols('x:z') == (x, y, z)
    assert symbols('a:d,x:z') == (a, b, c, d, x, y, z)
    assert symbols(('a:d', 'x:z')) == ((a, b, c, d), (x, y, z))


def test_call():
    f = Symbol('f')
    assert f(2)
    raises(TypeError, lambda: Wild('x')(1))
