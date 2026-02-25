# ✅ Todo REST API

A simple and clean REST API for managing todos, built with **Node.js**, **TypeScript**, and **Express**.

## 🚀 Getting Started

### 1. Install dependencies
```bash
npm install
```

### 2. Run in development mode
```bash
npm run dev
```

### 3. Build for production
```bash
npm run build
npm start
```

The server will start at `http://localhost:3000`

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/todos` | Get all todos |
| GET | `/todos?status=completed` | Get completed todos |
| GET | `/todos?status=pending` | Get pending todos |
| GET | `/todos/:id` | Get a single todo |
| POST | `/todos` | Create a new todo |
| PATCH | `/todos/:id` | Update a todo |
| DELETE | `/todos/:id` | Delete a todo |

---

## 📝 Examples

### Create a Todo
```bash
curl -X POST http://localhost:3000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Buy groceries", "description": "Milk, eggs, bread"}'
```

### Get All Todos
```bash
curl http://localhost:3000/todos
```

### Get Pending Todos
```bash
curl http://localhost:3000/todos?status=pending
```

### Mark as Completed
```bash
curl -X PATCH http://localhost:3000/todos/<id> \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

### Delete a Todo
```bash
curl -X DELETE http://localhost:3000/todos/<id>
```

---

## 🛠 Tech Stack

- **Node.js** - Runtime
- **TypeScript** - Type safety
- **Express** - Web framework
- **UUID** - Unique ID generation

## 📁 Project Structure

```
src/
├── index.ts    # Entry point & server setup
├── routes.ts   # API route handlers
├── store.ts    # In-memory data store
└── types.ts    # TypeScript interfaces
```

---

## 💡 Notes

- Data is stored **in-memory** and resets when the server restarts.
- To persist data, swap `store.ts` with a database like SQLite or PostgreSQL.
"# todo-api" 
