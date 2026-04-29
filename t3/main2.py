class Virta:
    def __init__(self):
        self.on = False

    def toggle(self):
        self.on = not self.on

class Valo:
    def __init__(self, sijainti):
        self.virta = Virta()
        self.kirkkaus = 0
        self.sijainti = sijainti

    def set_brightness(self, value):
        if 0 <= value <= 100:
            self.kirkkaus = value

    def is_on(self):
        return self.virta.on

class COMController:
    def __init__(self):
        self.valot = []
    def add_light(self, valo):
        self.valot.append(valo)
    def get_light(self, sijainti):
        for i in self.valot:
            if i.sijainti == sijainti:
                return i
        return None
    def show(self):
        print("LIGHT STATUS:")
        for i in self.valot:
            print(i.sijainti, "|", "ON" if i.is_on() else "OFF", "| brightness:", i.kirkkaus)

class User:
    def __init__(self, name, room, controller):
        self.name = name
        self.room = room
        self.controller = controller
    def toggle_light(self):
        light = self.controller.get_light(self.room)
        if light:
            light.virta.toggle()
    def set_brightness(self, value):
        light = self.controller.get_light(self.room)
        if light:
            light.set_brightness(value)
class Admin:
    def __init__(self, controller):
        self.controller = controller
    def show_all(self):
        self.controller.show()
    def toggle_any(self, room):
        light = self.controller.get_light(room)
        if light:
            light.virta.toggle()
    def set_any_brightness(self, room, value):
        light = self.controller.get_light(room)
        if light:
            light.set_brightness(value)
# enbsi käynnistys
controller = COMController()
# lights in system
controller.add_light(Valo("olohuone"))
controller.add_light(Valo("makuuhuone"))
controller.add_light(Valo("keittiö"))
# luo käyttäjät
users = [
    User("pena", "olohuone", controller),
    User("pekka", "makuuhuone", controller),
    User("paako", "keittiö", controller)
]
admin = Admin(controller)
# main
while True:
    print("")
    print("MENU")
    print("1 select user")
    print("2 admin")
    print("3 exit")
    choice = input("choose: ")
    #user
    if choice == "1":
        print("USERS:")
        for i, u in enumerate(users):
            print(i, "-", u.name, "(room:", u.room, ")")
        idx = int(input("select user: "))
        if 0 <= idx < len(users):
            user = users[idx]
            print("USER:", user.name)
            print("1 toggle light")
            print("2 set brightness")
            c = input("choice: ")
            if c == "1":
                user.toggle_light()
            elif c == "2":
                val = int(input("brightness (0-100): "))
                user.set_brightness(val)
    #admin
    elif choice == "2":
        print("")
        print("ADMIN")
        print("1 show all lights")
        print("2 toggle light")
        print("3 set brightness")

        c = input("choice: ")
        if c == "1":
            admin.show_all()
        elif c == "2":
            admin.show_all()
            room = input("room: ")
            admin.toggle_any(room)
        elif c == "3":
            admin.show_all()
            room = input("room: ")
            val = int(input("brightness (0-100): "))
            admin.set_any_brightness(room, val)
    elif choice == "3":
        break