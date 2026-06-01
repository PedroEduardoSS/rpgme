from models.hero_model import HeroModel

class HeroController:
    """
    Controller for hero page
    """

    def __init__(self, model=None):
        self.model = model or HeroModel

    def get_title(self):
        return "Hero"
