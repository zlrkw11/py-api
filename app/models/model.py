from pydantic import BaseModel, Field 

class Engine(BaseModel):
    horsepower: int = Field(..., gt=0)
    fuel_type: str 

class Vehicle(BaseModel):
    name: str
    brand: str
    price: float 
    engine: Engine
    
class Car(Vehicle):
    doors: int 
    type: str
    
