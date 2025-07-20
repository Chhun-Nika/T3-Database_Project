# create role 

CREATE ROLE 'admin';
GRANT ALL PRIVILEGES ON hospital.* TO 'admin';

CREATE ROLE 'data_analyst';
GRANT SELECT ON hospital.* TO 'data_analyst';

CREATE ROLE 'developer';
GRANT SELECT, INSERT, DELETE, CREATE ON hospital.* TO 'developer';

# database administrator
CREATE ROLE 'dba';
GRANT ALL PRIVILEGES ON hospital.* TO 'dba';

CREATE ROLE 'auditor';
GRANT SELECT ON hospital.* TO 'auditor';

CREATE ROLE 'qa_support';
GRANT SELECT, INSERT ON hospital.* TO 'qa_support';




