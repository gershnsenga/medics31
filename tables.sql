
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