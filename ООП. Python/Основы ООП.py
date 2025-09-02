class MLBB_hero:
    name = None
    class_ = None
    role = None
    have = None

    def __init__(self, name, class_, role, have): 
        self.set_data(name, class_, role, have)
        self.get_data()

    def set_data(self, name, class_, role, have):
        self.name = name
        self.class_ = class_
        self.role = role
        self.have = have

    def get_data(self):
        print(self.name, self.class_, self.role, self.have)
        

hero1 = MLBB_hero('Lapu-Lapu', 'fighter', 'exp-liner', False)


# hero1.set_data('Lapu-Lapu', 'fighter', 'exp-liner', False)
# hero1.get_data()


