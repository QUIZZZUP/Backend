from .db import db

class SimpleQuestion(db.Model):
    __tablename__ = 'simple_question'
    id = db.Column(db.String, primary_key=True)
    question = db.Column(db.String, nullable=False, unique=True)
    answer = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f'<SimpleQuestion {self.id}>\n\tquestion: {self.question}\n\tanswer: {self.answer}'
