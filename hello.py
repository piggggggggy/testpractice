class mon():
    hp = 100
    alive = True

    def damage(self, attack):
        self.hp = hp-attack
        if self.hp <0:
            self.alive = False

    def status(self):
        if self.alive ==True:
            print('삶')
        else:
            print('주금')
