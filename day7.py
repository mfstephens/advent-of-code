import numpy as np
    

class Gate(object):
    def __init__(self, inputs, operation, output):
        self.inputs = inputs
        self.operation = operation
        self.output = output

    def prettyPrint(self):
        print "inputs: {0}, operation: {1}, output: {2}".format(self.inputs, self.operation, self.output)

class Circuit(object):
    def __init__(self):
        self.circuit = {}

    def commandLengthThree(self, command):
        command = command.split()
        op1 = command[0]
        op3 = command[2]
        self.circuit[op3] = Gate([op1], None, op3)

    def commandLengthFour(self, command):
        command = command.split()
        op1 = command[0]
        op2 = command[1]
        op4 = command[3]
        self.circuit[op4] = Gate([op2], op1, op4)

    def commandLengthFive(self, command):
        command = command.split()
        op1 = command[0]
        op2 = command[1]
        op3 = command[2]
        op5 = command[4]
        self.circuit[op5] = Gate([op1, op3], op2, op5)

    def parseCommandsFromFile(self):
        f = open('day-7-input', 'r')
        for line in f:
            command = line.split()
            if len(command) == 3:
                self.commandLengthThree(line)
            elif len(command) == 4:
                self.commandLengthFour(line)
            elif len(command) == 5:
                self.commandLengthFive(line)

        self.circuit["b"] = Gate([np.uint16(46065)], None, "b")

        f.close()

    def doBitwiseOperation(self, operation, x, y=None):
        if operation == "AND":
            return np.bitwise_and(x, y)
        elif operation == "LSHIFT":
            return np.left_shift(x, y)
        elif operation == "RSHIFT":
            return np.right_shift(x, y)
        elif operation == "OR":
            return np.bitwise_or(x, y)
        elif operation == "NOT":
            return np.invert(x)
        else:
            return x

    def getFinalSignalForWire(self, wire):
        gate = self.circuit[wire]
        gate.prettyPrint()
        if len(gate.inputs) == 1:
            # check if we have a value for this gate's inputs
            input0 = gate.inputs[0]
            if type(input0) is np.uint16:
                return self.doBitwiseOperation(gate.operation, input0)
            elif input0.isdigit():
                gate.inputs[0] = np.uint16(gate.inputs[0])
                outputVal = self.doBitwiseOperation(gate.operation, gate.inputs[0])
                return outputVal
            else:
                gate.inputs[0] = np.uint16(self.getFinalSignalForWire(gate.inputs[0]))
                outputVal = self.doBitwiseOperation(gate.operation, gate.inputs[0])
                return outputVal
        elif len(gate.inputs) == 2:
            input0 = gate.inputs[0]
            input1 = gate.inputs[1]

            if type(input0) == str:
                if input0.isdigit():
                    input0 = np.uint16(input0)
                    gate.inputs[0] = input0
            if type(input1) == str:
                if input1.isdigit():
                    input1 = np.uint16(input1)
                    gate.inputs[1] = input1

            if type(input0) is np.uint16 and type(input1) is np.uint16:
                return self.doBitwiseOperation(gate.operation, input0, input1)
            if type(input0) is np.uint16 and type(input1) is not np.uint16:
                input1 = np.uint16(self.getFinalSignalForWire(input1))
                gate.inputs[1] = input1
            elif type(input0) is not np.uint16 and type(input1) is np.uint16:
                input0 = np.uint16(self.getFinalSignalForWire(input0))
                gate.inputs[0] = input0
            else:
                input0 = np.uint16(self.getFinalSignalForWire(input0))
                input1 = np.uint16(self.getFinalSignalForWire(input1))
                gate.inputs[0] = input0
                gate.inputs[1] = input1

            return self.doBitwiseOperation(gate.operation, input0, input1)



c = Circuit()
c.parseCommandsFromFile()
print c.getFinalSignalForWire("a")
