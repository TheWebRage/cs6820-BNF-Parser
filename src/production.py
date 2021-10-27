class Production:
    production = []

    def AddProduction(self, **kwargs):
        self.production = []

        for kw in kwargs:
            self.production.append(kw)