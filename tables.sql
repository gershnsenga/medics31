
--- Disease table

CREATE TABLE disease(
    id CHAR(36) PRIMARY KEY,
    disease_name VARCHAR(255) 
    );

ALTER TABLE disease ADD COLUMN description TEXT AFTER disease_name;

UPDATE disease SET description='One of the widely spread disease in this country and Africa.' WHERE id='d407f92f-ecfa-11ee-9842-0242ac110002';
--- Type table

ALTER TABLE disease ADD COLUMN is_widely BOOLEAN AFTER description;
UPDATE disease SET is_widely='true'

CREATE TABLE type (
    id CHAR(36)  PRIMARY KEY,
    type_name VARCHAR(255)
    );


--- DiseaseType join table

CREATE TABLE disease_type (
    id CHAR(36) PRIMARY KEY,
    disease_id CHAR(36),
    type_id CHAR(36),
    FOREIGN KEY (disease_id) REFERENCES disease(id),
    FOREIGN KEY (type_id) REFERENCES type(id)
);

SELECT disease.disease_name
FROM disease
JOIN disease_type ON disease.id = disease_type.disease_id;
--- Disease information table

CREATE TABLE disease_info (
    id CHAR(36) PRIMARY KEY,
    disease_id CHAR(36),
    preventions TEXT,
    treatment TEXT,
    FOREIGN KEY (disease_id) REFERENCES disease(id)
);


--- Gender table table
CREATE TABLE gender(
    id CHAR(36) PRIMARY KEY,
    gender_name ENUM('Male', 'Female', 'Other') NOT NULL
    );


--- Gender and disease join table 

CREATE TABLE disease_gender (
    id CHAR(36) PRIMARY KEY,
    disease_id CHAR(36),
    gender_id CHAR(36),
    FOREIGN KEY (disease_id) REFERENCES disease(id),
    FOREIGN KEY (gender_id) REFERENCES gender(id)
);


CREATE TABLE doctor(
    id CHAR(36) PRIMARY KEY, 
    name VARCHAR(55) NOT NULL,
    bio VARCHAR(1000),
    specialization VARCHAR(55) NOT NULL,
    phone VARCHAR(55) NOT NULL,
    email VARCHAR(55) NOT NULL,
    hospital VARCHAR(55) NOT NULL
    );

INSERT INTO doctor (id, name, bio,specialization, phone, email, hospital) VALUES
('550e8400-e29b-41d4-a716-446655440000', 'Dr. Peter Nmesoma', 'Desc : Meet Dr. Peter, a specialist in cardiology. For more information, use the contacts below to get in touch with him.', 'Cardiologist', '+250788123456', 'peter.doe@example.com', 'City Hospital'),
('550e8400-e29b-41d4-a716-446655440001', 'Dr. Tracy Murenzi', 'BIO', 'Pediatrician', '+250788234567', 'tracy.smith@example.com', 'Central Clinic'),
('550e8400-e29b-41d4-a716-446655440002', 'Dr. Jade Tuzinde','BIO' ,'Dermatologist', '+250788345678', 'jade.johnson@example.com', 'General Hospital'),
('550e8400-e29b-41d4-a716-446655440003', 'Dr. Jinelle', 'BIO' ,'Oncologist', '+250788456789', 'jinelle.williams@example.com', 'Regional Hospital');
