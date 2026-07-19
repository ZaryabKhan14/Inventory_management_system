class Purchase:

    def __init__(self,purchase_id,supplier_id,product_id,quantity,purchase_price,total_amount,purchase_date,payment_status,purchase_status,created_at,updated_at):
        

        self.purchase_id = purchase_id
        self.supplier_id = supplier_id
        self.product_id = product_id
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.total_amount = total_amount
        self.purchase_date = purchase_date
        self.payment_status = payment_status
        self.purchase_status = purchase_status
        self.created_at = created_at
        self.updated_at = updated_at
        
        pass