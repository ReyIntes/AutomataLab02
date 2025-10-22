class StateMachine:
    def __init__(self, binary_input):
        self.input = binary_input
        self.states = []
        self.outputs = []

    def display_transition_table(self):
        print("\nTransition Table:")
        print(f"{'Current State':<15}{'Input':<10}{'Next State':<15}{'Output':<10}")
        print("-" * 50)
        for i in range(len(self.input)):
            curr_state = self.states[i]
            next_state = self.states[i + 1] if i + 1 < len(self.states) else "-"
            output = self.outputs[i] if i < len(self.outputs) else "-"
            print(f"{curr_state:<15}{self.input[i]:<10}{next_state:<15}{output:<10}")


class MealyMachine(StateMachine):
    def process(self):
        # Simple Mealy logic: output depends on state + input
        state = 'A'
        self.states.append(state)

        for bit in self.input:
            if state == 'A':
                output = '0' if bit == '0' else '1'
                state = 'B' if bit == '1' else 'A'
            elif state == 'B':
                output = '1' if bit == '0' else '0'
                state = 'C' if bit == '0' else 'A'
            elif state == 'C':
                output = '1' if bit == '1' else '0'
                state = 'B' if bit == '1' else 'C'

            self.outputs.append(output)
            self.states.append(state)

        print("\n=== Mealy Machine Results ===")
        print(f"Input:  {self.input}")
        print(f"States: {' '.join(self.states)}")
        print(f"Output: {''.join(self.outputs)}")
        self.display_transition_table()


class MooreMachine(StateMachine):
    def process(self):
        # Simple Moore logic: output depends on state only
        state = 'A'
        self.states.append(state)

        output_map = {'A': '0', 'B': '1', 'C': '0'}

        for bit in self.input:
            if state == 'A':
                state = 'B' if bit == '1' else 'A'
            elif state == 'B':
                state = 'C' if bit == '0' else 'A'
            elif state == 'C':
                state = 'B' if bit == '1' else 'C'

            self.outputs.append(output_map[state])
            self.states.append(state)

        print("\n=== Moore Machine Results ===")
        print(f"Input:  {self.input}")
        print(f"States: {' '.join(self.states)}")
        print(f"Output: {''.join(self.outputs)}")
        self.display_transition_table()


# === Main Program ===
def main():
    print("Choose a machine type:")
    print("1. Mealy Machine")
    print("2. Moore Machine")

    choice = input("Enter your choice (1 or 2): ").strip()
    binary_input = input("Enter binary input (0s and 1s): ").strip()

    if not all(bit in "01" for bit in binary_input):
        print("Invalid input! Please enter only 0s and 1s.")
        return

    if choice == "1":
        machine = MealyMachine(binary_input)
        machine.process()
    elif choice == "2":
        machine = MooreMachine(binary_input)
        machine.process()
    else:
        print("Invalid choice! Please select 1 or 2.")


if __name__ == "__main__":
    main()
