from pydantic import BaseModel,EmailStr,Field

class CreateSupplierDTO(BaseModel):

    supplier_name : str = Field(...,min_length=2,max_length=150)
    supplier_email : EmailStr 
    supplier_contact : str = Field(..., pattern=r'^\+?[0-9]{10,15}$')
    supplier_address : str = Field(...,min_length=2,max_length=150)
    supplier_description : str = Field(...,min_length=2,max_length=150)
    supplier_status : str = Field(...,min_length=2,max_length=150)