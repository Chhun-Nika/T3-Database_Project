CREATE DATABASE hospital;
USE hospital;


-- Patient Table
CREATE TABLE Patient (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
  	last_name VARCHAR(100) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) UNIQUE,
    address VARCHAR(255),
    phone VARCHAR(20) NOT NULL,
    emergency_contact VARCHAR(100),
    emergency_contact_phone VARCHAR(20) NOT NULL,
    registration_date DATE DEFAULT (CURRENT_DATE)
);

-- Doctor Table
CREATE TABLE Doctor (
    doctor_id INT PRIMARY KEY AUTO_INCREMENT,
    dep_id INT NOT NULL, 
    first_name VARCHAR(100) NOT NULL,
  	last_name VARCHAR(100) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    dob DATE,
    specialization VARCHAR(100) NOT NULL,
    phone VARCHAR(15) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE NOT NULL,
    room_number VARCHAR(10)
);

-- Department table
CREATE TABLE Department (
	department_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR (100) NOT NULL,
    department_type VARCHAR(100),
    head_of_dep INT,
    location VARCHAR(100),
    FOREIGN KEY (head_of_dep) REFERENCES Doctor(doctor_id)
);


-- Nurse Table
CREATE TABLE Nurse (
    nurse_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
  	last_name VARCHAR(100) NOT NULL,
    gender ENUM('Male', 'Female', 'Other') NOT NULL,
    dob DATE,
    dep_id INT NOT NULL,
    shift ENUM('Morning', 'Evening', 'Night', 'Other') NOT NULL, 
    phone VARCHAR(20) NOT NULL,
    hire_date DATE NOT NULL,
    email VARCHAR(100) UNIQUE,
    FOREIGN KEY (dep_id) REFERENCES Department (department_id)
);

-- Appointment Table
CREATE TABLE Appointment (
    appointment_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_datetime DATETIME NOT NULL,
    reason TEXT,
    status ENUM('Scheduled', 'Completed', 'Cancelled', 'No-Show') DEFAULT 'Scheduled',
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id)
);

-- Medication Table
CREATE TABLE Medication (
    medication_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    expiration_date DATE
);

-- junction table between department and medication
CREATE TABLE DepartmentMedication (
    department_id INT,
    medication_id INT,
    -- make sure the stock quantity is a non-negative number
    stock_quantity INT UNSIGNED NOT NULL,
    PRIMARY KEY (department_id, medication_id),
    FOREIGN KEY (department_id) REFERENCES Department(department_id),
    FOREIGN KEY (medication_id) REFERENCES Medication(medication_id)
);


-- Medical_Record Table
CREATE TABLE Medical_Record (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    appointment_id INT,
    diagnosis TEXT,
    treatment TEXT,
    visit_date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (appointment_id) REFERENCES Appointment(appointment_id)
);

-- Prescription table
CREATE TABLE Prescription (
    prescription_id INT PRIMARY KEY AUTO_INCREMENT,
    medical_record_id INT NOT NULL,
    date_issued DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (medical_record_id) REFERENCES Medical_Record(record_id)
);


-- junction table between Prescription and medication
CREATE TABLE PrescriptionMedication (
    prescription_id INT,
    medication_id INT,
    dosage VARCHAR(50),
    frequency VARCHAR(50),
    duration VARCHAR(50),
    PRIMARY KEY (prescription_id, medication_id),
    FOREIGN KEY (prescription_id) REFERENCES Prescription(prescription_id),
    FOREIGN KEY (medication_id) REFERENCES Medication(medication_id)
);





-- Billing Table (drop)
CREATE TABLE Billing (
    bill_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    appointment_id INT NOT NULL,
    total_amount DECIMAL(10, 2),
    payment_status ENUM('Pending', 'Paid', 'Cancelled') DEFAULT 'Pending',
    billing_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    payment_method VARCHAR(50),
    FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (appointment_id) REFERENCES Appointment(appointment_id)
);

-- Room Table
CREATE TABLE Room (
    room_id INT PRIMARY KEY AUTO_INCREMENT,
    room_number VARCHAR(10) NOT NULL UNIQUE,
    room_type VARCHAR(50) NOT NULL, 
    availability_status ENUM('Available', 'Occupied', 'Maintenance') DEFAULT 'Available',
    assigned_patient_id INT,
    department_id INT,
    FOREIGN KEY (assigned_patient_id) REFERENCES Patient(patient_id),
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);

-- Receptionist
CREATE TABLE Receptionist (
    receptionist_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
  	last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE,
    hire_date DATE NOT NULL,
    shift ENUM('Morning', 'Evening', 'Night', 'Other'),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES Department(department_id)
);