"""
Pure Python TODO REST API
A simple REST API for managing todos with full CRUD operations
"""

from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory data store
todos = {}


class Todo:
    """Todo model"""
    def __init__(self, title, description=""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    def update(self, title=None, description=None, completed=None):
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if completed is not None:
            self.completed = completed
        self.updated_at = datetime.now().isoformat()


# ==================== API Routes ====================

@app.route('/todos', methods=['GET'])
def get_todos():
    """Get all todos with optional filtering by status"""
    status = request.args.get('status', None)
    
    result = list(todos.values())
    
    if status == 'completed':
        result = [todo for todo in result if todo.completed]
    elif status == 'pending':
        result = [todo for todo in result if not todo.completed]
    
    return jsonify([todo.to_dict() for todo in result]), 200


@app.route('/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Get a single todo by ID"""
    if todo_id not in todos:
        return jsonify({"error": "Todo not found"}), 404
    
    return jsonify(todos[todo_id].to_dict()), 200


@app.route('/todos', methods=['POST'])
def create_todo():
    """Create a new todo"""
    data = request.get_json()
    
    # Validation
    if not data:
        return jsonify({"error": "Request body required"}), 400
    
    if "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400
    
    # Create todo
    todo = Todo(
        title=data["title"],
        description=data.get("description", "")
    )
    
    todos[todo.id] = todo
    
    return jsonify(todo.to_dict()), 201


@app.route('/todos/<todo_id>', methods=['PATCH'])
def update_todo(todo_id):
    """Update a todo"""
    if todo_id not in todos:
        return jsonify({"error": "Todo not found"}), 404
    
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Request body required"}), 400
    
    todo = todos[todo_id]
    todo.update(
        title=data.get("title"),
        description=data.get("description"),
        completed=data.get("completed")
    )
    
    return jsonify(todo.to_dict()), 200


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    if todo_id not in todos:
        return jsonify({"error": "Todo not found"}), 404
    
    deleted_todo = todos.pop(todo_id)
    
    return jsonify(deleted_todo.to_dict()), 200


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "ok"}), 200


# ==================== Error Handlers ====================

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400


@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
