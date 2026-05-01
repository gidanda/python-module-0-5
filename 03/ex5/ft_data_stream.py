import typing 
import random

PLAYERS = [
    "alice",
    "bob",
    "charlie",
    "dylan",
]

ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "release",
    "use",
]

def gen_event():
    while True:
        name = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (name, action)

def consume_event(events):
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        event = events.pop(index)
        yield event

def main():
    print("=== Game Data Stream Processor ===")

    event_generator = gen_event()

    for i in range(1000):
        
        player, action = next(event_generator)
        print(f"Event {i}: Player {player} did action {action}")

    events = []

    for i in range(10):
        events.append(next(event_generator))

    print(f"Built list of 10 events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")

if __name__ == "__main__":
    main()