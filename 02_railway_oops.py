class RailwayForm:
    fromType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

gayatriApplication = RailwayForm()
gayatriApplication.name = "Gayatri"
gayatriApplication.train = "Rajdhani Express"
gayatriApplication.printData()