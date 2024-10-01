import sys
from north import NorthInterpreter

def main():
    print("Welcome to North REPL")
    interpreter = NorthInterpreter()  # Initialize your interpreter here
    while True:
        try:
            user_input = input("North> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            result = interpreter.run(user_input)
            print(result)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting North REPL.")
            break


def start_repl():
    """Start the North REPL."""
    interpreter = NorthInterpreter()
    print("North Interpreter REPL")
    print("Type 'exit' or Ctrl+C to quit")
    
    while True:
        try:
            # Prompt the user for input
            user_input = input(">> ")
            
            # Check if the user wants to exit
            if user_input.lower() in ['exit', 'quit']:
                print("Exiting REPL. Goodbye!")
                break
            
            # Run the input in the interpreter
            result = interpreter.run(user_input)
            
             # Print the result if any
            if result is not None:
                print(result)
            #print("Stack:", interpreter.stack)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting REPL. Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")

def run_file(file_path):
    """Run a North script from a file."""
    interpreter = NorthInterpreter()
    
    try:
        with open(file_path, 'r') as f:
            program = f.read()
            result = interpreter.run(program)
            print(result)
            # Optionally print the final state of the stack
            print("Final Stack:", interpreter.stack)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """Main function to handle REPL or file execution."""
    if len(sys.argv) == 1:
        # No file specified, start the REPL
        start_repl()
    elif len(sys.argv) == 2:
        # A file path is provided, run the script
        file_path = sys.argv[1]
        run_file(file_path)
    else:
        print("Usage:")
        print("  North           # Start the REPL")
        print("  North <file>    # Run a North script from a file")

if __name__ == "__main__":
    main()
