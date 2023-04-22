import sys
from twisted.internet.protocol import Protocol, Factory
from twisted.internet import reactor

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.hp = 10
        self.level = 1

    def __str__(self):
        return f"Name: {self.name}, HP: {self.hp}, Level: {self.level}, Inventory: {self.inventory}"

class DnDProtocol(Protocol):
    def connectionMade(self):
        print("New client connected")

    def connectionLost(self, reason):
        print("Client disconnected")

    def dataReceived(self, data):
        data = data.decode().strip()
        print(f"Received data: {data}")

        # Handle incoming commands
        if data == "create":
            self.factory.create_player(self.transport)
        elif data == "list":
            self.factory.list_players(self.transport)
        elif data.startswith("attack"):
            self.factory.attack_player(self.transport, data.split()[1])
        else:
            self.transport.write("Unknown command".encode())

class DnDFactory(Factory):
    def __init__(self):
        self.players = {}

    def create_player(self, transport):
        # Ask the player for their name
        transport.write("Enter your name: ".encode())
        name = yield from self.get_input(transport)

        # Create the player
        player = Player(name)
        self.players[transport] = player

        # Confirm creation
        transport.write(f"Player {name} created".encode())

    def list_players(self, transport):
        # List all connected players
        transport.write("Connected players:\n".encode())
        for player in self.players.values():
            transport.write(str(player).encode() + b"\n")

    def attack_player(self, transport, name):
        # Find the player to attack
        target = None
        for player in self.players.values():
            if player.name == name:
                target = player
                break

        if not target:
            transport.write(f"Player {name} not found".encode())
            return

        # Perform the attack
        target.hp -= 1
        transport.write(f"Player {target.name} attacked".encode())

    def buildProtocol(self, addr):
        return Dn
