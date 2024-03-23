from db.models import Customer
from db.session import use_session

def list_users():
    with use_session() as session:
        loans = session.query(Customer).all()
        loans_json = [loan.__json__() for loan in loans]
        return loans_json


def create_user(full_name: str, email: str):
    with use_session() as session:
        user = Customer(full_name=full_name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

def get_user(user_id: int):
    with use_session() as session:
        return session.query(Customer).filter(Customer.id == user_id).first()

def get_user_by_name(full_name: str):
    with use_session() as session:
        return session.query(Customer).filter(Customer.full_name == full_name).first()

def get_user_by_email(email: str):
    with use_session() as session:
        return session.query(Customer).filter(Customer.email == email).first()

def update_user(user_id: str, full_name: str, email: str):
    with use_session() as session:
        user = session.query(Customer).filter(Customer.id == user_id).first()
        if user:
            user.full_name = full_name
            user.email = email
            session.commit()
            session.refresh(user)
            return user

def delete_user(user_id: int):
    with use_session() as session:
        user = session.query(Customer).filter(Customer.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

def delete_user_by_name(full_name: str):
    with use_session() as session:
        user = session.query(Customer).filter(Customer.full_name == full_name).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False

def delete_user_by_email(email: str):
    with use_session() as session:
        user = session.query(Customer).filter(Customer.email == email).first()
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
