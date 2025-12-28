CREATE TABLE memberinfo (
  member_id VARCHAR(45) PRIMARY KEY,
  username VARCHAR(45),
  firstname VARCHAR(45),
  lastname VARCHAR(45),
  age INT,
  gender VARCHAR(45),
  email VARCHAR(45),
  phonenumber BIGINT
);

CREATE TABLE addressinfo (
  address_id VARCHAR(45) PRIMARY KEY,
  city VARCHAR(45),
  state VARCHAR(45),
  country VARCHAR(45),
  pincode VARCHAR(45),
  memberinfo_member_id VARCHAR(45),
  CONSTRAINT fk_addressinfo_memberinfo
    FOREIGN KEY (memberinfo_member_id)
    REFERENCES memberinfo(member_id)
);

CREATE TABLE cardiodiagnosis (
  cardio_id VARCHAR(45) PRIMARY KEY,
  cardioarrestdetected INT,
  date TIMESTAMP,
  memberinfo_member_id VARCHAR(45),
  CONSTRAINT fk_cardiodiagnosis_memberinfo
    FOREIGN KEY (memberinfo_member_id)
    REFERENCES memberinfo(member_id)
);

CREATE TABLE bloodtest (
  blood_id VARCHAR(45) PRIMARY KEY,
  date TIMESTAMP,
  bloodpressure INT,
  fbs INT,
  thal INT,
  serumcholesterol INT,
  cardiodiagnosis_cardio_id VARCHAR(45),
  CONSTRAINT fk_bloodtest_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE diseasedetail (
  disease_id VARCHAR(45) PRIMARY KEY,
  diagnoseddate TIMESTAMP,
  recovereddate TIMESTAMP,
  isrecovered BOOLEAN,
  cardiodiagnosis_cardio_id VARCHAR(45),
  CONSTRAINT fk_diseasedetail_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE ecgreport (
  ecg_id VARCHAR(45) PRIMARY KEY,
  date TIMESTAMP,
  restecg INT,
  cardiodiagnosis_cardio_id VARCHAR(45),
  CONSTRAINT fk_ecgreport_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE symptom (
  symptom_id VARCHAR(45) PRIMARY KEY,
  date TIMESTAMP,
  exang INT,
  oldpeak FLOAT,
  cp INT,
  cardiodiagnosis_cardio_id VARCHAR(45),
  CONSTRAINT fk_symptom_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE wearabledevicedata (
  wearable_device_id VARCHAR(45) PRIMARY KEY,
  thalach INT,
  slope INT,
  date TIMESTAMP,
  cardiodiagnosis_cardio_id VARCHAR(45),
  CONSTRAINT fk_wearabledevicedata_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);

CREATE TABLE xray (
  xray_id VARCHAR(45) PRIMARY KEY,
  date TIMESTAMP,
  ca INT,
  cardiodiagnosis_cardio_id VARCHAR(45),
  CONSTRAINT fk_xray_cardiodiagnosis
    FOREIGN KEY (cardiodiagnosis_cardio_id)
    REFERENCES cardiodiagnosis(cardio_id)
);
