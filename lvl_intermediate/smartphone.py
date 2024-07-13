class Phone:
    def __init__(self) -> None:
        pass

    def call(self):
        return "Calling..."
    
    def text(self):
        return "texting..."
    

class Camera:
    def __init__(self) -> None:
        pass

    def capture(self):
        return "capturing..."
    
class Player:
    def __init__(self) -> None:
        pass

    def plays(self):
        return "song is playing..."
    
class smartPhone(Phone, Camera, Player):
    pass

if __name__ == '__main__':
    sp = smartPhone()
    print(sp.call())
    print(sp.capture)
    