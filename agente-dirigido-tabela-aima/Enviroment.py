from Agent import Agent
from Thing import Thing

import numbers


class Environment:
    """Clase abstracta que representa un entorno. Clases de entorno 'real'
    heredar de esto. Normalmente, su entorno deberá implementar:
        percept:        define la percepción que ve un agente.
        execute_action: define los efectos de ejecutar una acción.
                           También actualice la ranura agent.performance.
    El entorno mantiene una lista de .cosas y .agentes (que es un subconjunto
    de cosas). Cada agente tiene una ranura .performance, inicializada a 0.
    Cada cosa tiene una ranura de ubicación, aunque algunos entornos pueden no
    necesito esto."""

    def __init__(self):
        self.things = []
        self.agents = []

    def thing_classes(self):
        return []  # Lista de clases que pueden ir al medio ambiente.

    def percept(self, agent):
        """Devuelve la percepción que el agente ve en este punto. (Implemente esto.)"""
        raise NotImplementedError

    def execute_action(self, agent, action):
        """Cambia el mundo para reflejar esta acción. (Implementar esto.)"""
        raise NotImplementedError

    def default_location(self, thing):
        """Ubicación predeterminada para colocar algo nuevo con una ubicación no especificada."""
        return None

    def exogenous_change(self):
        """Si hay un cambio espontáneo en el mundo, anótelo."""
        pass

    def is_done(self):
        """De forma predeterminada, terminamos cuando no podemos encontrar un agente activo."""
        return not any(agent.is_alive() for agent in self.agents)

    def step(self):
        """Ejecute el entorno por un paso de tiempo. Si el
        acciones y cambios exógenos son independientes, este método
        hacer. Si hay interacciones entre ellos, necesitará
        anule este método."""
        if not self.is_done():
            actions = []
            for agent in self.agents:
                if agent.alive:
                    actions.append(agent.program(self.percept(agent)))
                else:
                    actions.append("")
            for (agent, action) in zip(self.agents, actions):
                self.execute_action(agent, action)
            self.exogenous_change()

    def run(self, steps=1000):
        """Ejecute el entorno para un número determinado de pasos de tiempo."""
        for step in range(steps):
            if self.is_done():
                return
            self.step()

    def list_things_at(self, location, tclass=Thing):
        """Devuelve todas las cosas exactamente en una ubicación determinada."""
        if isinstance(location, numbers.Number):
            return [thing for thing in self.things
                    if thing.location == location and isinstance(thing, tclass)]
        return [thing for thing in self.things
                if all(x == y for x, y in zip(thing.location, location)) and isinstance(thing, tclass)]

    def some_things_at(self, location, tclass=Thing):
        """Devuelve verdadero si al menos una de las cosas en la ubicación
        es una instancia de la clase tclass (o una subclase)."""
        return self.list_things_at(location, tclass) != []

    def add_thing(self, thing, location=None):
        """Agregue algo al entorno, estableciendo su ubicación. Para
        conveniencia, si algo es un programa de agente, hacemos un nuevo agente
        para ello. (No debería ser necesario anular esto)."""
        if not isinstance(thing, Thing):
            thing = Agent(thing)
        if thing in self.things:
            print("No puedo agregar lo mismo dos veces")
        else:
            thing.location = location if location is not None else self.default_location(
                thing)
            self.things.append(thing)
            if isinstance(thing, Agent):
                thing.performance = 0
                self.agents.append(thing)

    def delete_thing(self, thing):
        """Elimina algo del medio ambiente."""
        try:
            self.things.remove(thing)
        except ValueError as e:
            print(e)
            print("  en el entorno delete_thing")
            print("  Cosa que debe eliminarse: {} at {}".format(
                thing, thing.location))
            print("  de la lista: {}".format(
                [(thing, thing.location) for thing in self.things]))
        if thing in self.agents:
            self.agents.remove(thing)
