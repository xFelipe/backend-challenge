"""
2.- Utilizando a mesma estrutura do banco de dados da questão anterior, 
rescreva a consulta anterior utilizando um ORM (Object Relational Mapping) 
de sua preferência utilizando a query language padrão do ORM adotado 
(ex.: Spring JOOQ, EEF LINQ, SQL Alchemy Expression Language, etc).
"""
from sqlalchemy.sql.expression import select
from db import Session
from models import Claim, Role, User


query = (
    select(
        User.name.label('nome'),
        User.email.label('e-mail'),
        Role.description.label('descrição do papel'),
        Claim.description.label('descrições das permissões')
    )
    .join(User.claims)
    .join(User.role)
)

with Session() as session:
    rows = [*session.execute(query)]
    print(rows)
