CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    def __init__(self, channels):
        self.channels = channels
        # індекс каналу починається з 0
        self.current_index = 0

    def first_channel(self):
        self.current_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_index = n - 1
        return self.current_channel()

    def next_channel(self):
        # якщо це останній канал, переходимо до першого (індекс 0)
        if self.current_index == len(self.channels) - 1:
            self.current_index = 0
        else:
            self.current_index += 1
        return self.current_channel()

    def previous_channel(self):
        # якщо це перший канал, переходимо до останнього
        if self.current_index == 0:
            self.current_index = len(self.channels) - 1
        else:
            self.current_index -= 1
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_index]

    def exists(self, query):
        # перевірка чи query є числом (номер) чи рядком (назва)
        if isinstance(query, int):
            if 1 <= query <= len(self.channels):
                return "Yes"
        elif isinstance(query, str):
            if query in self.channels:
                return "Yes"
        return "No"

controller = TVController(CHANNELS)

print(f"1. First: {controller.first_channel()}")          # BBC
print(f"2. Last: {controller.last_channel()}")            # TV1000
print(f"3. Turn 1: {controller.turn_channel(1)}")         # BBC
print(f"4. Next: {controller.next_channel()}")            # Discovery
print(f"5. Previous: {controller.previous_channel()}")    # BBC
print(f"6. Current: {controller.current_channel()}")      # BBC
print(f"7. Exists 4: {controller.exists(4)}")             # No
print(f"8. Exists 'BBC': {controller.exists('BBC')}")     # Yes