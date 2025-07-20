# tables are generated via sequelize

INSERT INTO roles (name, description, createdAt, updatedAt) VALUES
('admin', 'Full access to the hospital database including user and privilege managemen', NOW(), NOW()),
('data_analyst', 'Read-only access to query and analyze hospital data', NOW(), NOW()),
('developer', 'Can view, insert, delete, and create records and structures for development purposes', NOW(), NOW()),
('dba', 'Database administrator with superuser access to all operations and configurations', NOW(), NOW()),
('auditor', 'Read-only access to monitor and audit data for compliance and security', NOW(), NOW()),
('qa_support', 'Can view and insert test data to verify system behavior without affecting production', NOW(), NOW());

INSERT INTO privileges (resource, action, createdAt, updatedAt)
VALUES 
  ('*', 'CREATE', NOW(), NOW()),
  ('*', 'READ', NOW(), NOW()),
  ('*', 'UPDATE', NOW(), NOW()),
  ('*', 'DELETE', NOW(), NOW()),
  ('*', 'ALL PRIVILEGES', NOW(), NOW());  