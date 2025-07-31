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

    def receive_call(self, from_user):
        print(f"{self.name} received a call from {from_user.name}.")
        self.in_call = True
        from_user.in_call = True
        print(f"Call started between {self.name} and {from_user.name}.")

    def end_call(self, other_user):
        print(f"{self.name} ended the call with {other_user.name}.")
        self.in_call = False
        other_user.in_call = False

# Example usage
if __name__ == "__main__":
    alice = User("Alice")
    bob = User("Bob")

    alice.call(bob)         # Alice calls Bob
    alice.end_call(bob)     # Alice ends the call
