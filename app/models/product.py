class Product:

    def __init__(self,product_id,product_name,quantity_in_stock,product_purchase_price,product_selling_price,product_description,product_status,created_at,updated_at,category_id,supplier_id,product_code,unit):

        self.product_id = product_id
        self.product_name = product_name
        self.quantity_in_stock = quantity_in_stock
        self.product_price = product_purchase_price
        self.product_selling_price = product_selling_price
        self.product_description = product_description
        self.product_status = product_status
        self.created_at = created_at
        self.updated_at = updated_at
        self.category_id = category_id
        self.supplier_id = supplier_id
        self.product_code = product_code
        self.unit = unit

        