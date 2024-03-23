from db.models import Loan
from db.session import use_session
from db.models import Loan

def list_loan():
    with use_session() as session:
        loans = session.query(Loan).all()
        loans_json = [loan.__json__() for loan in loans]
        return loans_json

def create_loan(amount: float, customer_id: str):
    with use_session() as session:
        new_loan = Loan(amount=amount, customer_id=customer_id)
        session.add(new_loan)
        session.commit()
        session.refresh(new_loan)
        return new_loan
    

def get_loan(loan_id: str):
    with use_session() as session:
        return session.query(Loan).filter(Loan.id == loan_id).first()

def update_loan(loan_id: str, amount: float):
    with use_session() as session:
        loan = session.query(Loan).filter(Loan.id == loan_id).first()
        loan.amount = amount
        session.commit()
        session.refresh(loan)
        return loan

def delete_loan(loan_id: int):
    with use_session() as session:
        loan = session.query(Loan).filter(Loan.id == loan_id).first()
        session.delete(loan)
        session.commit()
