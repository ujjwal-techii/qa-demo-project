class User:
    def __init__(self, name):
        self.name = name
        self.in_call = False

    def call(self, other_user):
        if not other_user.in_call:
            print(f"{self.name} is calling {other_user.name}...")
            other_user.receive_call(self)
        else:
            print(f"{other_user.name} is already on another call.")



# Example usage
if __name__ == "__main__":
    alice = User("Alice")
    bob = User("Bob")

    alice.call(bob)         # Alice calls Bob
    alice.end_call(bob)     # Alice ends the call
