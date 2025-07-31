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


import time
from datetime import datetime

class CallSession:
    def __init__(self, caller, receiver):
        self.caller = caller
        self.receiver = receiver
        self.start_time = None
        self.end_time = None

    def start_call(self):
        if self.receiver.in_call:
            print(f"{self.receiver.name} is already on another call.")
            return False
        print(f"{self.caller.name} is calling {self.receiver.name}...")
        self.start_time = datetime.now()
        self.caller.in_call = True
        self.receiver.in_call = True
        print(f"📞 Call started at {self.start_time.strftime('%H:%M:%S')}")
        return True

    def end_call(self):
        self.end_time = datetime.now()
        self.caller.in_call = False
        self.receiver.in_call = False
        duration = (self.end_time - self.start_time).seconds
        print(f"📴 Call ended at {self.end_time.strftime('%H:%M:%S')}. Duration: {duration} seconds.")

class User:
    def __init__(self, name):
        self.name = name
        self.in_call = False

    def initiate_call(self, other_user):
        session = CallSession(self, other_user)
        if session.start_call():
            time.sleep(2)  # Simulate 2-second call
            session.end_call()

# ------------------------------
# Run the simulation
# ------------------------------
if __name__ == "__main__":
    user1 = User("Haseeb")
    user2 = User("Zoya")

    user1.initiate_call(user2)
