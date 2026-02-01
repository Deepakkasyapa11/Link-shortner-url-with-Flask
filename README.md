# LinkNode | High-Performance URL Shortening Service

A robust, production-ready Flask microservice designed for low-latency URL redirection and click-stream analytics. This project demonstrates modern Python web development patterns, moving away from volatile memory storage to a persistent, relational database architecture.
<img width="592" height="623" alt="Screenshot (135)" src="https://github.com/user-attachments/assets/23cf32d4-eb98-4fc7-9466-57f9923b3e35" />

# Architectural Design
Unlike standard boilerplate implementations, this project utilizes a **Modular Factory Pattern** to ensure scalability and ease of testing.

* **Application Factory:** Decouples the Flask instance creation from the global scope, preventing circular dependencies.
* **Persistence Layer:** Utilizes SQLAlchemy ORM for ACID-compliant data transactions.
* **Collision Resistance:** Uses `secrets.token_urlsafe` to generate high-entropy, URL-safe identifiers, minimizing the risk of ID collisions.
* **Analytics Engine:** Integrated a streamlined redirection pipeline that captures real-time click metrics.

# Tech Stack
- **Backend:** Flask 3.x
- **ORM:** SQLAlchemy (Relational Mapping)
- **Database:** SQLite (Engineered for seamless migration to PostgreSQL/MySQL)
- **Tooling:** Python 3.8+, Virtualenv

# Getting Started

### 1. Environment Setup
```bash
# Clone the repository
git clone <your-repo-url>
cd link-shortner-flask

# Initialize virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

2. Dependency Management
pip install -r requirements.txt
3. Execution
# The application automatically initializes the SQLite database on first run
python run.py
The service will be available at http://127.0.0.1:5000.

# Design Decisions
Manual Form Handling: Opted for raw request parsing over external libraries like Flask-WTF to reduce overhead and demonstrate core HTTP protocol understanding.

Data Isolation: Designed a dedicated Link model with unique constraints on the short_id to ensure data integrity.

Security: Implemented CSRF-resistant patterns and secure secret key management via a dedicated config.py.
