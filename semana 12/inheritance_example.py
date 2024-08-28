class Dance:
    def dancing(self):
        print("Im dancing")


class Sing:
    def singing(self):
        print("While Im singing")



class Artist(Dance, Sing):
    pass



david_bisbal = Artist()
david_bisbal.dancing()
david_bisbal.singing()