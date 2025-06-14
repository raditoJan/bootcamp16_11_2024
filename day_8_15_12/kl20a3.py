class NotFound(Exception):
    def __init__(self, resource, resource_id):
        msg = f"{resource} o ID {resource_id} nie znaleziono"
        super().__init__(msg)
        self.resource = resource
        self.resource_id = resource_id

    @classmethod
    def user(cls, user_id):
        return cls("Użytkownik", user_id)

    @staticmethod
    def for_any(resource, resource_id):
        return NotFound(resource, resource_id)

# raise NotFound.user(7)  # Dla użytkownika
raise NotFound.for_any("Dokument", 10)  # Dla dowolnego zasobu