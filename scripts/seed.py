from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Base, User, Discipline, Rating

engine = create_engine('sqlite:///smash.db')
Session = sessionmaker(bind=engine)
session = Session()

def quick_test():
    clash = session.query(Discipline).filter_by(name='clash_royale').first()
    if not clash:
        clash = Discipline(name='clash_royale')
        session.add(clash)
        session.commit()

    vlad = session.query(User).filter_by(display_name='Vlad').first()
    if not vlad:
        vlad = User(display_name='Vlad')
        session.add(vlad)
        session.commit()

    rating = session.query(Rating).filter_by(user_id=vlad.id, discipline_id=clash.id).first()
    if not rating:
        rating = Rating(user_id=vlad.id, discipline_id=clash.id, elo=1000.0)
        session.add(rating)
        session.commit()

    print(f"Success! User {vlad.display_name} has {rating.elo} Elo in {clash.name}")

if __name__ == "__main__":
    quick_test()