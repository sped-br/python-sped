import doctest

from sped import campos
from sped import erros
from sped import registros

assert doctest.testmod(campos)
assert doctest.testmod(erros)
assert doctest.testmod(registros)
