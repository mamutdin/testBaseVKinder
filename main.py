import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = sq.create_engine('postgresql+psycopg2://postgres:A84db68d@localhost:5432/vkinder')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Initiator(Base):
    __tablename__ = 'initiators'

    id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    bdate = sq.Column(sq.String)
    id_sex = sq.Column(sq.Integer)
    city = sq.Column(sq.String)
    found = relationship("Favourite")

class FoundPeople(Base):
    __tablename__ = 'found_people'

    id = sq.Column(sq.Integer, primary_key=True)
    first_name = sq.Column(sq.String)
    last_name = sq.Column(sq.String)
    bdate = sq.Column(sq.String)
    id_sex = sq.Column(sq.Integer)
    city = sq.Column(sq.String)
    initiators = relationship("Favourite")

class Favourite(Base):
    __tablename__ = 'favourite'

    id = sq.Column(sq.Integer, primary_key=True)
    initiator_id = sq.Column(sq.Integer, sq.ForeignKey('initiators.id'))
    found_id = sq.Column(sq.Integer, sq.ForeignKey('found_people.id'))



if __name__ == '__main__':
    session = Session()
    # Base.metadata.create_all(engine)
    # query = session.query(Initiator)
    smbd = Initiator(first_name='Ramil', city='Moscow')
    smbd2 = Initiator(first_name='ivan', id_sex=1)
    session.add_all([smbd, smbd2])
    session.commit()