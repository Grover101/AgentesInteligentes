from Enviroment import Environment

import random


class TrivialVacuumEnvironment(Environment):
    """Este entorno tiene dos ubicaciones, A y B. Cada una puede estar sucia
    o Limpiar. El agente percibe su ubicación y la ubicación
    estado. Esto sirve como un ejemplo de cómo implementar un sencillo
    Medio ambiente."""

    loc_A, loc_B = (0, 0), (1, 0)  # The two locations for the Vacuum world

    def __init__(self):
        super().__init__()
        self.status = {self.loc_A: random.choice(['Limpia', 'Sucio']),
                       self.loc_B: random.choice(['Limpia', 'Sucio'])}

    def thing_classes(self):
        # return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent, TableDrivenVacuumAgent, ModelBasedVacuumAgent]
        return []

    def percept(self, agent):
        """Devuelve la ubicación del agente y el estado de la ubicación (sucio / limpio)."""
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        """Cambiar la ubicación del agente y / o el estado de la ubicación; seguimiento del rendimiento.
        Puntuación 10 por cada suciedad limpiada; -1 por cada movimiento."""
        if action == 'Derecha':
            agent.location = self.loc_B
            agent.performance -= 1
        elif action == 'Izquierda':
            agent.location = self.loc_A
            agent.performance -= 1
        elif action == 'Chupar':
            if self.status[agent.location] == 'Sucio':
                agent.performance += 10
            self.status[agent.location] = 'Limpia'

    def default_location(self, thing):
        """Los agentes comienzan en cualquier lugar al azar."""
        return random.choice([self.loc_A, self.loc_B])
