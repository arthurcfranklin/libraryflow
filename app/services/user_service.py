from sqlalchemy.orm import Session
from app.models.user import User


def list_users(db: Session):
    return db.query(User).all()


def create_user(
    db: Session,
    name: str,
    email: str,
    registration: str
):
    user = User(
        name=name,
        email=email,
        registration=registration,
        status="Ativo"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        db.delete(user)
        db.commit()

    return user


def update_user(
    db: Session,
    user_id: int,
    name: str,
    email: str,
    registration: str,
    status: str
):
    user = db.query(User).filter(User.id == user_id).first()

    if user:
        user.name = name
        user.email = email
        user.registration = registration
        user.status = status

        db.commit()
        db.refresh(user)

    return user