# T3-Database_Project: Hospital Management System (HMS)

## Introduction
This is a database project for a Hospital Management System (HMS), developed to manage core hospital operations like patient registration, appointment scheduling, medical records, billing, and staff coordination. The system helps hospitals reduce paperwork, avoid errors, and improve communication by using a centralized and digital solution.
<br><br>
## Project Structure

Here’s what you’ll find in this repository:

- `pythonScript/` — python scripts to populate the database with sample data.
- `MySQL_script/` — sql scripts to:
  - Create tables
  - Execute queries
  - Set up roles and permissions
- `RBAC/` — Web-based Role-Based Access Control system:
  - `client/` — Frontend built with React.js
  - `server/` — Backend using Node.js, Express, Sequelize
- `Report_Slide/` — Final report and presentation slides related to the project.
<br><br>
## Getting Started

Follow these steps to set up and run the web-based RBAC system.

### 1. Clone the Repository

```bash
git clone https://github.com/Chhun-Nika/T3-Database_Project
cd RBAC
```

### 2. Set up Environment Variables

```bash
cp .env.example .env
```
Example of .env format 

```bash
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=hms_db
DB_PORT=3306

JWT_SECRET=your_jwt_secret
```

### 3. Install Dependencies

Backend Setup
```bash
cd server
npm install
```

Frontend Setup
```bash
cd ../client
npm install
```

### 4. Run the Application
Start Backend
```bash
cd ../server
npm run dev
```

Start Frontend
```bash
cd ../client
npm start
```
## Additional Notes
- Ensure MySQL is installed and running
- Use the scripts in `MySQL_script/` to set up your database schema and initial roles
- Use `pythonScript/` to insert sample records
- The app uses Sequelize ORM and JWT-based authentication
<br><br>
## Project Report and Slide
Report and slide are in PDF format inside `Report_Slide/` folder


