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



class User:
    def __init__(self, name):
        self.name = name
        self.in_call = False
def initiate_call(self, other_user):
        print(f"{self.name} is trying to call {other_user.name}...")
        call_session = CallSession(self, other_user)
        if call_session.start_call():
            time.sleep(2)  # Simulate call duration
            self.end_call(other_user)


def end_call(self, other_user):


    def burgering(self, other_user):
        if not self.in_call or not other_user.in_call:
            print(f"Call cannot be ended. Either {self.name} or {other_user.name} is not in a call.")
            return
        self.in_call = False
        other_user.in_call = False
        end_time = datetime.now()
        duration = (end_time - self.start_time).seconds
        print(f"📞 Call ended at {end_time.strftime('%H:%M:%S')}. Duration: {duration} seconds.")



# ------------------------------
# Run the simulation
# ------------------------------
if __name__ == "__main__":
    user1 = User("Haseeb")
    user2 = User("Zoya")

    user1.initiate_call(user2)
