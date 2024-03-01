
import sqlalchemy
from .db_session import SqlAlchemyBase

from sqlalchemy import orm

# id
# team_leader (id) (id руководителя, целое число)
# job (description) (описание работы)
# work_size (hours) (объем работы в часах)
# collaborators (list of id of participants) (список id участников)
# start_date (дата начала)
# end_date (дата окончания)
# is_finished (bool) (признак завершения)


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer)
    job = sqlalchemy.Column(sqlalchemy.String)
    work_size = sqlalchemy.Column(sqlalchemy.Integer)
    collaborators = orm.relationship("id")
    start_date = sqlalchemy.Column(sqlalchemy.String)
    end_date = sqlalchemy.Column(sqlalchemy.String)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean)
