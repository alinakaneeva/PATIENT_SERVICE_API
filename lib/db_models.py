
""" Responsible for creating the Database Models
# SQLAlchemy uses the term "model" to refer to these classes 
# and instances that interact with the database.
"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import mapped_column, relationship
from .database_connection import Base

# Note:
# SQLAlchemy models define attributes
# using =, and pass the type as a parameter to Column
# i.e name = Column(String)

class Physician(Base):
    __tablename__ = "physician"
    id = Column(Integer, primary_key=True)
    specialty = Column(String)
    patients = relationship('Patient', backref='physician')

class Patient(Base):
    __tablename__ = "patient"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    ssn = Column(String, nullable=False)
    gender = Column(String)
    address = Column(String)
    physician_id = Column(Integer, ForeignKey('physician.id'))
    insurances = relationship('Insurance', backref='patient')

class Appointment(Base):
    __tablename__ = "appointment"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    appointment_date = Column(Date, nullable=False)
    description = Column(String, nullable=False)
    physician_id = Column(Integer, ForeignKey('physician.id'))   

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))   

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    ssn = Column(String, nullable=False)
    position = Column(String)
    hospital_id = Column(Integer, ForeignKey('hospital.id'))   
    department_id = Column(Integer, ForeignKey('department.id'))    

class Hospital(Base):
    __tablename__ = "hospital"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)

class Insurance(Base):
    __tablename__ = "insurance"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    provider_name = Column(String, nullable=False)
    policy_number = Column(String, nullable=False)

class Manager(Base) :
    __tablename__ = "manager"
    id = Column(Integer, primary_key=True)  

class Medication(Base):
    __tablename__ = "medication"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    brand = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Nurse(Base) :
    __tablename__ = "nurse"
    id = Column(Integer, primary_key=True)
    qualification = Column(String) 

class Prescription(Base):
    __tablename__ = "prescription"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    prescibing_physician_id = Column(Integer,nullable=False )
    medication_id = Column(Integer,ForeignKey('medication.id') )
    prescription_date = Column(Date, nullable=False)
    quantity = Column(Integer, nullable=False)
    dosage = Column(String)
    frequency = Column(String)
    start_date = Column(Date)
    end_date =  Column(Date)
    refills_available = Column(Integer, nullable=False)   

class Room(Base) :
    __tablename__ = "room"
    id = Column(Integer, primary_key=True)
    room_type_id = Column(Integer, nullable=False)
    available = Column(Boolean, nullable=False)    

class Room_Type(Base) :
    __tablename__ = "room_type"
    id = Column(Integer, primary_key=True)
    type = Column(String)