from Thing import Thing

import collections


class Agent(Thing):
    """ Un agente es una subclase de Thing con un atributo de instancia obligatorio
    (también conocido como slot), .program, que debe contener una función que tome un argumento,
    la percepción, y devuelve una acción. (Lo que cuenta como percepción o acción
    dependerá del entorno específico en el que exista el agente).
    Tenga en cuenta que "programa" es una ranura, no un método. Si fuera un método, entonces el
    El programa podría "engañar" y observar aspectos del agente. No se supone
    para hacer eso: el programa solo puede mirar las percepciones. Un programa de agentes
    que necesita un modelo del mundo (y del propio agente) tendrá que
    construir y mantener su propio modelo. Hay una ranura opcional, .performance,
    que es un número que da la medida de desempeño del agente en su
    medio ambiente."""

    def __init__(self, program=None):
        self.alive = True
        self.bump = False
        self.holding = []
        self.performance = 0
        # si el programa es Ninguno o no es instancia (program, collections.abc.Callable):
        if program is None or not isinstance(program, collections.Callable):
            print("No puedo encontrar un programa válido para {}, cayendo de nuevo al valor predeterminado.".format(
                self.__class__.__name__))

            def program(percept):
                return eval(input('Percept={}; action? '.format(percept)))

        self.program = program

    def can_grab(self, thing):
        """Devuelve True si este agente puede tomar esta cosa.
        Anular para las subclases apropiadas de Agente y Cosa."""
        return False
