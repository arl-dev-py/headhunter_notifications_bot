from sqlalchemy.orm import Session
from database.db import session
from database.models import Vacancies
from sqlalchemy import select, update, delete


class CheckVac:
    def __init__(self, session: Session):
        self.session = session

    def create(self, vac_id):
        vacancies = Vacancies(vac_id=vac_id)
        self.session.add(vacancies)
        self.session.commit()

    def checker(self, id):
        stmt = select(Vacancies).where(Vacancies.vac_id == id)
        result = self.session.execute(stmt)
        return True if result.scalar_one_or_none() else False

    def update(self, id, vac_id):
        stmt = update(Vacancies).where(Vacancies.vac_id == id).values(vac_id = vac_id)
        self.session.execute(stmt)
        self.session.commit()
        self.session.close()

    def delete(self, id):
        stmt = delete(Vacancies).where(Vacancies.id == id)
        self.session.execute(stmt)
        self.session.commit()
        self.session.close()

    def close(self):
        self.session.close()