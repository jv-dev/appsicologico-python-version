class ConflictException(Exception):
    def __init__(self, message="Conflict: Resource already exists"):
        self.message = message
        super().__init__(self.message)