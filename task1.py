from queue import Queue
import random

request_queue = Queue()
request_counter = 0


def generate_request():
    global request_counter
    request_counter += 1
    request = {
        "id": request_counter,
        "type": random.choice(["repair", "consultation", "warranty"]),
    }
    request_queue.put(request)
    print(f"Generated request #{request['id']} | type: {request['type']}")


def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing request #{request['id']} | type: {request['type']}")
    else:
        print("Queue is empty - no requests to process.")


def main():
    print("Service Center Simulation")
    print("Commands: 'a' - add request, 'p' - process request, 'q' - quit\n")

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "a":
            generate_request()
        elif command == "p":
            process_request()
        elif command == "q":
            print("Exiting. Goodbye!")
            break
        else:
            print("Unknown command. Use 'a', 'p', or 'q'.")


if __name__ == "__main__":
    main()
