from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from builder import build_query
from models import RequestSchema

main_bp = Blueprint('main', __name__)

@main_bp.route('/perform_query', methods=['POST'])
def perform_query():
    data = request.json
    try:
        validated_data = RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400
    result = None
    for query in validated_data['queries']:
        result = build_query(
        cmd=query['cmd'],
        value=query['value'],
        file_name=validated_data['file_name'],
        data=result,
        )

    return jsonify(result)
