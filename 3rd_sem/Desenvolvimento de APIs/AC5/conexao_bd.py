from sqlalchemy import create_engine

#arquivo somente para conectar no banco de dados sqlite

def getConexao():
    engine = create_engine('sqlite:///escola_ac5.db') 
    return engine