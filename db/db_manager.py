import os
from sqlalchemy import create_engine, Column, String, Integer, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Default to SQLite for easy local dev; replace with Postgres/MySQL URI in prod
DB_URI = os.getenv("DATABASE_URL", "sqlite:///bug_tracker.db")
engine = create_engine(DB_URI)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

class TestRun(Base):
    __tablename__ = 'test_runs'
    # Capturing test results: Test Case ID, Status, Error Message, Timestamp [cite: 2]
    test_case_id = Column(String(50), primary_key=True)
    module = Column(String(50))
    status = Column(String(10), nullable=False)
    error_message = Column(Text)
    run_timestamp = Column(DateTime, default=datetime.utcnow)

class Bug(Base):
    __tablename__ = 'bugs'
    # Bug table fields: BugID, TestCaseID, Severity, Priority, Timestamp, Status [cite: 4]
    bug_id = Column(Integer, primary_key=True, autoincrement=True)
    test_case_id = Column(String(50))
    severity = Column(String(20), nullable=False)
    priority = Column(String(20), nullable=False)
    status = Column(String(20), default='Open')
    developer = Column(String(50), default='Unassigned')
    sprint = Column(String(20), default='Sprint 1')
    resolution_time_days = Column(Integer, nullable=True)
    logged_timestamp = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(engine)

def log_test_result(test_id, module, status, error=None):
    session = SessionLocal()
    run = TestRun(test_case_id=test_id, module=module, status=status, error_message=error)
    session.merge(run) # Update if exists, insert if new
    session.commit()
    session.close()

def log_bug(test_id, severity, priority):
    session = SessionLocal()
    bug = Bug(test_case_id=test_id, severity=severity, priority=priority)
    session.add(bug)
    session.commit()
    session.close()