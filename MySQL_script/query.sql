# Join

# 1. List all appointments with patient and doctor full names and their status
SELECT 
    a.appointment_id,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
    a.appointment_datetime,
    a.status
FROM Appointment a
JOIN Patient p ON a.patient_id = p.patient_id
JOIN Doctor d ON a.doctor_id = d.doctor_id;

# 2. List doctors and their departments
SELECT 
    CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
    dept.name AS department_name
FROM Doctor d
JOIN Department dept ON d.dep_id = dept.department_id;

# 3. List rooms and the patient assigned 
SELECT 
    r.room_number,
    r.room_type,
    r.availability_status,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name
FROM Room r
LEFT JOIN Patient p ON r.assigned_patient_id = p.patient_id;

# Sub-query

# 4. Get all patients who had appointment with a doctor specializing in 'Cardiology'
SELECT * FROM Patient
WHERE patient_id IN (
    SELECT a.patient_id
    FROM Appointment a
    JOIN Doctor d ON a.doctor_id = d.doctor_id
    WHERE d.specialization = 'Cardiology'
);

# 5. List patients who have more than 3 appointments
SELECT * FROM Patient
WHERE patient_id IN (
    SELECT patient_id FROM Appointment
    GROUP BY patient_id
    HAVING COUNT(*) > 3
);

# 6. Get departments with more than 1 doctor
SELECT * FROM Department
WHERE department_id IN (
    SELECT dep_id FROM Doctor
    GROUP BY dep_id
    HAVING COUNT(*) > 1
);

# Aggregation

# 7. Total billing amount per patient
SELECT 
    b.patient_id,
    CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    p.email,
    p.phone,
    SUM(b.total_amount) AS total_billed
FROM Billing b
JOIN Patient p ON b.patient_id = p.patient_id
GROUP BY b.patient_id, p.first_name, p.last_name, p.email, p.phone;

# 8. Count of medication types per department
SELECT 
    d.department_id,
    d.name AS department_name,
    COUNT(dm.medication_id) AS total_medication_types
FROM DepartmentMedication dm
JOIN Department d ON dm.department_id = d.department_id
GROUP BY d.department_id, d.name;

# 9. Count Total Appointments per Doctor
SELECT 
    d.doctor_id,
    CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
    COUNT(a.appointment_id) AS total_appointments
FROM Doctor d
JOIN Appointment a ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id;

# Function 
# 10. Calculate Age Function

DELIMITER //

CREATE FUNCTION calculate_age(dob DATE) RETURNS INT
DETERMINISTIC
BEGIN
    RETURN TIMESTAMPDIFF(YEAR, dob, CURDATE());
END //

DELIMITER ;

# test function
SELECT 
    patient_id,
    CONCAT(first_name, ' ', last_name) AS name,
    calculate_age(dob) AS age
FROM Patient;

# 11. Calculate Discounted Bill Function

DELIMITER //

CREATE FUNCTION calculate_discounted_bill(original_amount DECIMAL(10,2), discount_percent INT)
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE discounted_amount DECIMAL(10,2);
    SET discounted_amount = original_amount - (original_amount * discount_percent / 100);
    RETURN discounted_amount;
END //

DELIMITER ;

# test function
SELECT 
    bill_id,
    total_amount,
    calculate_discounted_bill(total_amount, 10) 
    AS discounted_total
FROM Billing;

# Triggers

# 12. Prevent Negative Stock in DepartmentMedication

DELIMITER //

CREATE TRIGGER prevent_negative_stock
BEFORE INSERT ON DepartmentMedication
FOR EACH ROW
BEGIN
    IF NEW.stock_quantity < 0 THEN
        SIGNAL SQLSTATE '45000' 
        SET MESSAGE_TEXT = 'Stock quantity cannot be negative';
    END IF;
END //

DELIMITER ;

# 13. Auto-Update Medication Stock After Prescription

DELIMITER //

CREATE TRIGGER update_stock_after_prescription
AFTER INSERT ON PrescriptionMedication
FOR EACH ROW
BEGIN
    DECLARE dep_id INT;

    SELECT d.dep_id
    INTO dep_id
    FROM Prescription p
    JOIN Medical_Record mr ON p.medical_record_id = mr.record_id
    JOIN Appointment a ON mr.appointment_id = a.appointment_id
    JOIN Doctor d ON a.doctor_id = d.doctor_id
    WHERE p.prescription_id = NEW.prescription_id;

    UPDATE DepartmentMedication
    SET stock_quantity = stock_quantity - 1
    WHERE medication_id = NEW.medication_id
      AND department_id = dep_id;
END;
//

DELIMITER ;

# Procedure

# 14. Get doctor’s appointments

DELIMITER //

CREATE PROCEDURE get_doctor_appointments(IN doc_id INT)
BEGIN
    SELECT * FROM Appointment
    WHERE doctor_id = doc_id
    ORDER BY appointment_datetime DESC;
END;
//

DELIMITER ;

# 15. Add medication and Stock

DELIMITER //

CREATE PROCEDURE add_medication_and_stock(
    IN med_name VARCHAR(100),
    IN dep_id INT,
    IN stock INT,
    IN price DECIMAL(10,2),
    IN expiry DATE
)
BEGIN
    DECLARE med_id INT;

    INSERT INTO Medication(name, unit_price, expiration_date)
    VALUES (med_name, price, expiry);

    SET med_id = LAST_INSERT_ID();

    INSERT INTO DepartmentMedication(department_id, medication_id, stock_quantity)
    VALUES (dep_id, med_id, stock);
END;
//

DELIMITER ;

















