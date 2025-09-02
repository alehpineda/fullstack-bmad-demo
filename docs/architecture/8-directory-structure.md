## 8. Directory Structure

The project will be organized in a monorepo structure:

```
/
├── .github/
│   └── workflows/
│       ├── ci.yaml
│       └── frontend-ci.yaml
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── crud.py
│   │   └── database.py
│   ├── scripts/
│   │   └── populate_db.py
│   ├── tests/
│   ├── pyproject.toml
│   └── README.md
├── docs/
│   └── architecture.md
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── tailwind.config.js
├── .gitignore
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
└── README.md
```
