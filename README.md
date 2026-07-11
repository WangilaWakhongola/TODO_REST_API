#  Python TODO REST API

Simple REST API for managing todos with full CRUD operations.

##  Quick Start

```bash
# 1. Create virtual environment
python3 -m venv 
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run API
python app.py
```

Server starts at: `http://localhost:3000`

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos` | Get all todos |
| GET | `/todos?status=pending` | Get pending todos |
| GET | `/todos/{id}` | Get single todo |
| POST | `/todos` | Create new todo |
| PATCH | `/todos/{id}` | Update todo |
| DELETE | `/todos/{id}` | Delete todo |

##  Examples

**Create a Todo:**
```bash
curl -X POST http://localhost:3000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

**Get All Todos:**
```bash
curl http://localhost:3000/todos
```

**Mark as Completed:**
```bash
curl -X PATCH http://localhost:3000/todos/{id} \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

**Delete Todo:**
```bash
curl -X DELETE http://localhost:3000/todos/{id}
```

## 🛠 Tech Stack

- Python 3.8+
- Flask
- UUID for IDs
- In-memory storage

##  To Add Database

Replace the `todos` dictionary in `app.py` with:
- SQLite + SQLAlchemy
- PostgreSQL
- MongoDB

---

Author : Wakhongola!
