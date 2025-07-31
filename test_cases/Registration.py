class User:
    def __init__(self, name):
        self.name = name
        self.in_call = False





# Example usage
if __name__ == "__main__":
    alice = User("Alice")
    bob = User("Bob")

    alice.call(bob)         # Alice calls Bob
    alice.end_call(bob)     # Alice ends the call




