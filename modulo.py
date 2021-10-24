#  import random Dessa forma você importa tudo o que tem dentro do módulo.
#  Para ver o que tem dentro do módulo, segure ctrl + botão esquerdo do mouse.

#  importa tudo do módulo.


from random import randint
from pacote.subPastaPacote import principalSubPasta as ps
from pacote import (
    # principal as pr,
    secundario as se,
    outro as ot
)
from pacote.principal import soma as sm
print(randint(1, 5))
print(sm(5, 5))
print(se.quadratica(5))
print(ot.cubica(3))
print(ps.multiplicacao(3, 5))
