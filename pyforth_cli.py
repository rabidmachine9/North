import sys
from pyforth import ForthInterpreter

def main():
    print("Welcome to PyForth REPL")
    interpreter = ForthInterpreter()  # Initialize your interpreter here
    while True:
        try:
            user_input = input("forth> ")
            if user_input.lower() in ["exit", "quit"]:
                break
            result = interpreter.run(user_input)
            print(result)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting PyForth REPL.")
            break


def start_repl():
    """Start the Forth REPL."""
    interpreter = ForthInterpreter()
    print("Forth Interpreter REPL")
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
    """Run a Forth script from a file."""
    interpreter = ForthInterpreter()
    
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
        print("  forth           # Start the REPL")
        print("  forth <file>    # Run a Forth script from a file")

if __name__ == "__main__":
    main()
