
--- Disease table

CREATE TABLE disease(
    id CHAR(36) PRIMARY KEY,
    disease_name VARCHAR(255) 
    );


--- Type table

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


--- Disease information table

CREATE TABLE disease_info (
    id CHAR(36) PRIMARY KEY,
    disease_id CHAR(36),
    preventions TEXT,
    treatment TEXT,
    FOREIGN KEY (disease_id) REFERENCES disease(id)
);


--- Gender table table
CREATE TABLE Gender(
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