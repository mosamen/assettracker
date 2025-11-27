from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.api.deps import get_db
from app.schemas.asset import Asset, AssetCreate, AssetUpdate
from app.crud import asset as crud_asset
from app.models.asset import AssetStatus

router = APIRouter()

@router.post("/", response_model=Asset, status_code=201)
def create_asset(
    asset: AssetCreate,
    db: Session = Depends(get_db)
):
    """Create a new asset"""
    if asset.serial_number:
        existing = crud_asset.get_asset_by_serial(db, asset.serial_number)
        if existing:
            raise HTTPException(status_code=400, detail="Asset with this serial number already exists")
    
    return crud_asset.create_asset(db, asset)

@router.get("/", response_model=List[Asset])
def read_assets(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    category: Optional[str] = None,
    status: Optional[AssetStatus] = None,
    db: Session = Depends(get_db)
):
    """Get all assets with optional filters"""
    assets = crud_asset.get_assets(db, skip=skip, limit=limit, category=category, status=status)
    return assets

@router.get("/search", response_model=List[Asset])
def search_assets(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    """Search assets by name, model, or serial number"""
    return crud_asset.search_assets(db, q)

@router.get("/{asset_id}", response_model=Asset)
def read_asset(
    asset_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific asset by ID"""
    asset = crud_asset.get_asset(db, asset_id)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@router.put("/{asset_id}", response_model=Asset)
def update_asset(
    asset_id: int,
    asset_update: AssetUpdate,
    db: Session = Depends(get_db)
):
    """Update an asset"""
    asset = crud_asset.update_asset(db, asset_id, asset_update)
    if not asset:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset

@router.delete("/{asset_id}", status_code=204)
def delete_asset(
    asset_id: int,
    db: Session = Depends(get_db)
):
    """Delete an asset"""
    success = crud_asset.delete_asset(db, asset_id)
    if not success:
        raise HTTPException(status_code=404, detail="Asset not found")
    return None
