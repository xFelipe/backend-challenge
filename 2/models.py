from re import A
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql.schema import Table

Base = declarative_base()

user_claims = Table('user_claims', Base.metadata,
        Column('user_id', ForeignKey('users.id'), primary_key=True),
        Column('claim_id', ForeignKey('claims.id'), primary_key=True)
)

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    description = Column(String)

    def __repr__(self):
        return (f'<Role '
                    f'id={self.id}, '
                    f'description={self.description} />')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship('Role')
    claims = relationship('Claim', secondary=user_claims, back_populates='users')
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    def __repr__(self):
        return (f'<User '
                    f'id={self.id}, '
                    f'name={self.name}, '
                    f'email={self.email}, '
                    f'password={self.password}, '
                    f'created_at={self.created_at}, '
                    f'updated_at={self.updated_at}, '
                    f'role={self.role}, '
                    f'claims={self.claims}, '
                    f'role_id={self.role_id} />')

class Claim(Base):
    __tablename__ = 'claims'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    active = Column(Boolean)
    users = relationship('User', secondary=user_claims, back_populates='claims')

    def __repr__(self):
        return (
            f'<Role '
                f'id={self.id}, '
                f'description={self.description} />'
        )
