import uuid
from typing import List
from uuid import UUID

from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError

from models.simple_question import SimpleQuestion, db

simple_question_bp = Blueprint('simple_question_bp', __name__)

@simple_question_bp.route('/simple_question', methods=['GET'])
def list_simple_questions():
    questions: List[SimpleQuestion] = SimpleQuestion.query.all()
    if len(questions) == 0:
        return []
    return [question.id for question in questions]

@simple_question_bp.route('/simple_question', methods=['POST'])
def add_question():
    data = request.get_json()

    if not data or 'question' not in data or 'answer' not in data:
        return jsonify({"error": "Missing 'question' or 'answer' in JSON"}), 400

    new_question = SimpleQuestion(id=uuid.uuid4().__str__(), question=data['question'], answer=data['answer'])

    try:
        db.session.add(new_question)
        db.session.commit()
    except IntegrityError:
        return jsonify({"error": "Question already exists"}), 400

    return jsonify({"message": "Question and answer received", "status": "success"}), 201

@simple_question_bp.route('/simple_question&id=<uuid:idx>', methods=['GET'])
def get_single_simple_question(idx: UUID):
    return SimpleQuestion.query.get(idx)
