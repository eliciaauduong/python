from abc import abstractmethod, ABC
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP Scroll")

    def click(self):
        pass

class DELL(TouchScreenLaptop):
    def scroll(self):
        print("DELL Scroll")

    def click(self):
        pass

class HPNotebook(HP):
    def click(self):
        print("HP Click")

class DELLNotebook(DELL):
    def click(self):
        print("DELL Click")


hp1 = HPNotebook()
hp1.scroll()
hp1.click()

dell1 = DELLNotebook()
dell1.scroll()
dell1.click()