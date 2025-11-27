from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class AssetStatus(str, enum.Enum):
    IN_USE = "in_use"
    AVAILABLE = "available"
    MAINTENANCE = "maintenance"
    RETIRED = "retired"

class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)  # laptop, tablet, tv, switch, etc.
    manufacturer = Column(String, nullable=True)
    model = Column(String, nullable=True)
    serial_number = Column(String, unique=True, nullable=True, index=True)
    status = Column(Enum(AssetStatus), default=AssetStatus.AVAILABLE)
    assigned_to = Column(String, nullable=True)  # Person or department
    location = Column(String, nullable=True)  # Room/building for mapping later
    purchase_date = Column(DateTime, nullable=True)
    warranty_expiry = Column(DateTime, nullable=True)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
