#Person (Humans/Zombies)
class Person:
    wasVaccinated : bool = False
    turnsVaccinated : int = 0
    isVaccinated : bool= False
    isZombie : bool = False
    wasCured : bool = False
    
    #Initialization method for the Person Class
    def __init__(self, iz):
        self.isZombie = iz

    #Creates a Copy of the Person class
    def clone(self):
        ret = Person(self.isZombie)
        ret.wasVaccinated = self.wasVaccinated
        ret.turnsVaccinated = self.turnsVaccinated
        ret.isVaccinated = self.isVaccinated
        ret.wasCured = self.wasCured
        return ret

    #(Moved from Board.py) Calc infection returns the chance that a person gets infected.  Modify numbers to alter chance of infection 
    def calcInfection(self):
        chance = 100
        if self.isVaccinated == True:
            chance -= 70
        if self.wasCured == True:
            chance -= 10
        return chance

    #Helper method to remove vaccination status, alter (if self.turnsVaccinated > x) to change vaccination timer
    def vaccinationWearOff(self):
        self.turnsVaccinated += 1
        if self.turnsVaccinated > 3:
            self.isVaccinated = False

    def __str__(self) -> str:
        return f"Person who is a zombie? {self.isZombie}"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, __o: object) -> bool:
        if type(__o) == Person:
            return (
                self.wasVaccinated == __o.wasVaccinated
                and self.turnsVaccinated == __o.turnsVaccinated
                and self.isVaccinated == __o.isVaccinated
                and self.isZombie == __o.isZombie
                and self.wasCured == __o.wasCured
            )
        return False
