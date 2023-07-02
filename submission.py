class Circuit:
    def __init__(self):
        self.A = False
        self.B = False
        self.C = False
        self.D = False
        self.net_e = False
        self.net_f = False
        self.net_g = False
        self.Z = False
    
    def evaluate(self, netlist):
        for line in netlist:
            line= line.split('=')
            lhs= line[0]
            rhs= line[1]
            if '&' in rhs:
                self.lhs = getattr(self, rhs.split('&')[0].strip()) and getattr(self, rhs.split('&')[1].strip())
            elif '|' in rhs:
                self.lhs = getattr(self, rhs.split('|')[0].strip()) or getattr(self, rhs.split('|')[1].strip())
            elif '~' in rhs:
                self.lhs = not getattr(self, rhs.split('~')[1].strip())
            elif '^' in rhs:
                self.lhs = getattr(self, rhs.split('^')[0].strip()) ^ getattr(self, rhs.split('^')[1].strip())
            setattr(self, lhs, self.lhs)


class PODEM:
    def __init__(self, circuit, fault_net, fault_type):
        self.circuit = circuit
        self.fault_net = fault_net
        self.fault_type = fault_type
        self.assignments = []
        self.inputs = {
            'A': False,
            'B': False,
            'C': False,
            'D': False
        }

    def run(self):
        self.initialize()
        result = self.backtrace()
        return self.assignments if result else []

    def initialize(self):
        if self.fault_type == 'SA0':
            self.inputs[self.fault_net] = True
        elif self.fault_type == 'SA1':
            self.inputs[self.fault_net] = False

    def backtrace(self):
        self.circuit.evaluate(netlist)

        if self.circuit.Z == (self.fault_type == 'SA0'):
            self.assignments = [(input_net, self.inputs[input_net]) for input_net in self.inputs]
            return True
        elif self.circuit.Z == (self.fault_type == 'SA1'):
            return False

        obj, d_frontier = self.select_path()
        if not obj:
            return False

        for obj_val in d_frontier:
            self.inputs[obj] = obj_val

            result = self.backtrace()
            if result:
                return True

        return False

    def select_path(self):
        d_frontier = []
        for input_net in self.inputs:
            if input_net not in self.assignments:
                d_frontier.append(input_net)

        if not d_frontier:
            return None, None

        return d_frontier[0], [False, True]


# Main program
with open('input.txt', 'r') as file2:
    netlist= file2.readlines() 

circuit = Circuit()

# Read fault details from file
with open('fault.txt', 'r') as file:
    fault_details = file.readlines()

fault_net = fault_details[0].strip().split('=')[1].strip()
fault_type = fault_details[1].strip().split('=')[1].strip()

podem = PODEM(circuit, fault_net, fault_type)
assignments = podem.run()

# Set the value of C as 1
for i in range(len(assignments)):
    if assignments[i][0] == 'C':
        assignments[i] = ('C', True)

# Open the output file
with open ('output.txt','w') as file3:
    key_list=[]
    value_list=[]
    for input_net, value in assignments:
        if len(input_net)==1:
            key_list.append(input_net)
            value_list.append(int(value))
    file3.write(str(key_list))
    file3.write(str(value_list))
    circuit.evaluate(netlist)
    str= f", Z= {int(circuit.Z)}"
    file3.write(str)

print("Input vector for fault testing:")
for input_net, value in assignments:
    print(f"{input_net}: {int(value)}")

print("Expected value of output for fault confirmation:")
circuit.evaluate(netlist)
print(f"Z: {int(circuit.Z)}")
