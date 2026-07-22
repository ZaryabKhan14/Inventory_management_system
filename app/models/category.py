class Category:

    def __init__(self,category_name,category_description,category_status,created_at=None,updated_at=None,category_id=None):

        self.category_id = category_id
        self.category_name = category_name
        self.category_description = category_description
        self.category_status = category_status
        self.created_at = created_at
        self.updated_at = updated_at