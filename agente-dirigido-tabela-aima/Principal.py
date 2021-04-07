from Agent import Agent
from Enviroment import Environment
from Thing import Thing
from TrivialVacuumEnvironment import TrivialVacuumEnvironment


def TableDrivenAgentProgram(table):
    percepts = []

    def program(percept):
        percepts.append(percept)
        action = table.get(tuple(percepts))
        return action
    return program


def TableDrivenVacuumAgent():
    # Las dos ubicaciones para el mundo de Vacuum
    loc_A, loc_B = (0, 0), (1, 0)
    table = {((loc_A, 'Limpia'),): 'Derecha',
             ((loc_A, 'Sucio'),): 'Chupar',
             ((loc_B, 'Limpia'),): 'Izquierda',
             ((loc_B, 'Sucio'),): 'Chupar',
             ((loc_A, 'Sucio'), (loc_A, 'Limpia')): 'Derecha',
             ((loc_A, 'Limpia'), (loc_B, 'Sucio')): 'Chupar',
             ((loc_B, 'Limpia'), (loc_A, 'Sucio')): 'Chupar',
             ((loc_B, 'Sucio'), (loc_B, 'Limpia')): 'Izquierda',
             ((loc_A, 'Sucio'), (loc_A, 'Limpia'), (loc_B, 'Sucio')): 'Chupar',
             ((loc_B, 'Sucio'), (loc_B, 'Limpia'), (loc_A, 'Sucio')): 'Chupar'}
    return Agent(TableDrivenAgentProgram(table))


agente = TableDrivenVacuumAgent()
ambiente = TrivialVacuumEnvironment()
ambiente.add_thing(agente)
ambiente.run()
print("Resultado : {}" .format(ambiente.status ==
                               {(1, 0): 'Limpia', (0, 0): 'Limpia'}))
