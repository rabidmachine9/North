class NorthInterpreter:
    def __init__(self):
        self.stack = []
        self.variables = {}  # Dictionary for variable storage
        self.functions = {}  # Dictionary for storing user-defined functions
        self.is_defining_function = False
        self.current_function_name = ""
        self.current_function_body = []
        #self.command_iterator = iter([])  # Initialize an empty command iterator
        self.commands = []
        self.current_index = 0
        
    def push(self, value):
        """Push a number (int or float) onto the stack."""
        try:
            self.stack.append(float(value))
        except ValueError:
            raise ValueError(f"Cannot push '{value}' onto the stack.")

    def add(self):
        """Pop two values from the stack, add, and push the result."""
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for addition")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a + b)

    def subtract(self):
        """Pop two values from the stack, subtract, and push the result."""
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for subtraction")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a - b)

    def dup(self):
        """Duplicate the top value on the stack."""
        if not self.stack:
            raise ValueError("Stack is empty, cannot duplicate")
        self.stack.append(self.stack[-1])  # Push a copy of the top stack value

    def multiply(self):
        """Pop two values from the stack, multiply, and push the result."""
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for multiplication")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a * b)
    
    def divide(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for division")
        b = self.stack.pop()
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        a = self.stack.pop()
        self.stack.append(a / b)

    def modulo(self):
        """Pop two values from the stack, get remainder, and push the result."""
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for multiplication")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(a % b)

    def set_variable(self, var_name):
        """Assign the top stack value to a variable."""
        if not self.stack:
            raise ValueError("Stack is empty")
        self.variables[var_name] = self.stack.pop()

    def get_variable(self, var_name):
        """Push the value of a variable onto the stack."""
        if var_name not in self.variables:
            raise ValueError(f"Undefined variable '{var_name}'")
        self.stack.append(self.variables[var_name])

    def define_function(self, function_name):
        """Begin defining a function."""
        self.is_defining_function = True
        self.current_function_name = function_name
        self.current_function_body = []

    def end_function_definition(self):
        """End the function definition."""
        self.is_defining_function = False
        self.functions[self.current_function_name] = self.current_function_body
        self.current_function_name = ""
        self.current_function_body = []

    def call_function(self, function_name):
        """Call and execute a defined function."""
        if function_name not in self.functions:
            raise ValueError(f"Undefined function '{function_name}'")
        for command in self.functions[function_name]:
            self.execute(command)

    # boolean
    def logic_equals(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for comparison")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(float(a == b))

    def logic_not_equals(self):
        """Pop two values from the stack, compare if they are not equal, and push the result."""
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for not equal operation")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(float(a != b))

    def logic_and(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for and operation")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(float(bool(a) and bool(b)))

    def logic_not(self):
        if not self.stack:
            raise ValueError("Stack is empty for not operation")
        a = self.stack.pop()
        self.stack.append(float(not bool(a)))

    def greater_than(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for comparison")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(float(a > b))

    def less_than(self):
        if len(self.stack) < 2:
            raise ValueError("Not enough values on the stack for comparison")
        b = self.stack.pop()
        a = self.stack.pop()
        self.stack.append(float(a < b))


    # 'if' statement implementation
    def if_statement(self):
        """Process an 'if-else-then' structure."""
        if len(self.stack) == 0:
            raise ValueError("Stack is empty, cannot perform 'if' operation.")
        
        condition = self.stack.pop()
        commands_if = []
        commands_else = []
        is_else = False

        # Collect commands until 'then' is found
        while self.current_index < len(self.commands):
            self.current_index += 1  # Move to the next command
            command = self.commands[self.current_index]

            if command == "then":
                break
            elif command == "else":
                is_else = True
            elif is_else:
                commands_else.append(command)
            else:
                commands_if.append(command)

        # Execute the appropriate branch
        if condition != 0:
            for cmd in commands_if:
                self.execute(cmd)
        else:
            for cmd in commands_else:
                self.execute(cmd)


    def execute(self, command):
        """Parse and execute a single command or token."""
        # Function definition mode: collecting function body
        if self.is_defining_function:
            if command == ";":  # End function definition
                print(f"Ending function definition: {self.current_function_name}")
                self.end_function_definition()
            elif not self.current_function_name:  # Capture function name
                self.current_function_name = command
                print(f"Captured function name: {command}")
            else:
                print(f"Appending to function {self.current_function_name}: {command}")
                self.current_function_body.append(command)
            return

        # Handle numbers
        try:
            self.push(float(command))  # If the command is a number, push it onto the stack
            return  # No need to continue further if it's a number
        except ValueError:
            pass  # Not a number, continue checking other commands

        # If ":" is encountered, begin function definition mode
        if command == ":": 
            self.is_defining_function = True
            print("Starting function definition")
            return


        # Conditional branching
        if command == "if":
            self.if_statement()  # Call the if-else handling logic
            return
        
        # Operators
        if command == "+":
            self.add()
        elif command == "-":
            self.subtract()
        elif command == "*":  # Add the * (multiply) command here
            self.multiply()
        elif command == "/":  # Add the * (multiply) command here
            self.divide()
        elif command == "%":  # Add the * (multiply) command here
            self.modulo()
        elif command == "dup":  # Add the dup command here
            self.dup()

        #boolean
        elif command == "=":
            self.logic_equals()
        elif command == "<>":
            not self.logic_not_equals()
        elif command == "and":
            self.logic_and()
        elif command == "not":
            self.logic_not()
        elif command == ">":
            self.greater_than()
        elif command == "<":
            self.less_than()


        # Handle variables
        elif command in self.variables:
            self.get_variable(command)
        elif command.startswith(":"):
            self.set_variable(command[1:])

        # Function execution
        elif command in self.functions:
            print(f"Calling function: {command}")
            self.call_function(command)

        # Raise an error for unknown commands
        else:
            raise ValueError(f"Unknown command: {command}")
    
    def run(self, program):
        """Run the Forth program."""
        # Split the program into lines first
        lines = program.splitlines()
        self.commands = []  # Clear previous commands
        for line in lines:
            # Check for a comment in the line and remove everything after '\'
            if "\\" in line:
                line = line.split("\\", 1)[0]  # Keep only the part before the comment
            self.commands.extend(line.split())  # Store commands in self.commands
           # Process all commands using index tracking
        self.current_index = 0
        while self.current_index < len(self.commands):
            command = self.commands[self.current_index]
            self.execute(command)
            self.current_index += 1  # Move to the next command

        # Final result after all operations
        if len(self.stack) == 1:
            return self.stack.pop()  # Return the final result
        elif len(self.stack) > 1:
            while len(self.stack) > 1:
                self.execute(command)
            return self.stack.pop()  # Return the final result
        else:
            raise ValueError("The stack is empty and no result could be produced.")
