# from pprintpp import pprint as pp
from db.database import Graph
from helper.write_a_json import write_a_json as wj

db = Graph(uri='bolt://44.193.223.228:7687', user='neo4j', password='bushings-secretary-parenthesis')

# Questão 01
# A
aux = db.execute_query('MATCH (n:Teacher WHERE n.name = "Renzo") RETURN(n.ano_nasc),(n.cpf)')    

wj(aux, '1A')

# B
aux = db.execute_query('MATCH (n:Teacher WHERE n.name =~ "M.*") RETURN(n.name),(n.cpf)')    

wj(aux, '1B')

# C
aux = db.execute_query('MATCH (n:City) RETURN(n)')    

wj(aux, '1C')

# D
aux = db.execute_query('MATCH (n:School WHERE n.number >= 150 OR n.number <= 550) RETURN(n.name),(n.address),(n.number)')    

wj(aux, '1D')

# Questão 02
# A
aux = db.execute_query('MATCH (n:Teacher) RETURN MIN(n.ano_nasc),MAX(n.ano_nasc)')    

wj(aux, '2A')

# B
aux = db.execute_query('MATCH (n:City) RETURN AVG(n.population)')    

wj(aux, '2B')

# C
aux = db.execute_query('MATCH (n:City WHERE n.cep = "37540-000") RETURN REPLACE(n.name, "a", "A")')    

wj(aux, '2C')

# D
aux = db.execute_query('MATCH (n:Teacher) RETURN RIGHT(n.name, 3)')    

wj(aux, '2D')

# Questão 03

def divider():
    print('\n' + '-' * 80 + '\n')

# A
class TeacherCRUD(object):
    def __init__(self):
        self.db = Graph(uri='bolt://44.193.223.228:7687',
                        user='neo4j', password='bushings-secretary-parenthesis')
    
    def create(self, name, ano_nasc, cpf):
        return self.db.execute_query('CREATE (n:Teacher {name:$name, ano_nasc:$ano_nasc, cpf:$cpf}) return n',
                                     {'name': teacher['name'], 'ano_nasc': teacher['ano_nasc'], 'cpf': teacher['cpf']})

    def read_by_name(self, name):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) RETURN n',
                                     {'name': teacher['name']})

    def delete(self, name):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) DELETE n',
                                     {'name': teacher['name']})        

    def update_cpf(self, name, newCpf):
        return self.db.execute_query('MATCH (n:Teacher {name:$name}) SET n.cpf = $cpf RETURN n',
                                     {'name': teacher['name'], 'cpf': teacher['cpf']})                         
    

# B

teacher = {
    name: 'Chris Lima',
    ano_nasc: 1956,
    cpf: '189.052.396-66' 
}

aux = dao.create(teacher)
pp(aux)
divider()

# C
name = 'Chris Lima'
aux = dao.read_by_name(name)
pp(aux)
divider()

# D
name = 'Chris Lima'
newCpf = '162.052.777-77'
aux = dao.update_cpf(name, newCpf)
pp(aux)
divider()