# Google_Girl_Hackathon_Final_Round
The problem statement for the Final Round was as follows:
The task is to design an algorithm and write its code to identify the input vector required to identify the fault at a given node in a given circuit.
In a case, there would only be a single fault in the design.
The algorithm should be efficient, robust and able to identify faults quickly.

<ins>Inputs</ins>
Available inputs are -
  1.Circuit file (format provided below)
  2.Fault node location
  3.Fault type
    a)SA0 : stuck-at-0, a fault where node is not able to attain value 1, irrespective of inputs
    b)SA1 : stuck-at-1, a fault where node is not able to attain value 0, irrespective of inputs
<ins>Outputs</ins>
The code should print a vector for inputs to test the fault, and the expected value of output to confirm the fault.
The output should be printed to the following file in run directory - output.txt

<ins>Circuit Format </ins>
  1.The circuit will have 4 inputs - A, B, C and D. All of which are boolean type (only 0 and 1 are valid inputs)
  2.The circuit’s output will always be Z which is also a boolean.
  3.The circuit will be built using the following operations -
    a)AND ( & ) gate
    b)OR ( | ) gate
    c)NOT ( ~ ) gate
    d)XOR ( ^ ) gate
  4.The circuit would purely be a combinational logic.
  5.All internal nodes in the circuit would be named as : “net_<alphanumeric string>”
  6.Each input ( A / B / C / D ) would be utilized only once in the circuit.

<ins>Example Input </ins>

Circuit File:
net_e = A & B
net_f = C | D
net_g = ~ net_f
Z = net_g ^ net_e

Fault:
FAULT_AT = net_f
FAULT_TYPE = SA0

Example Output:
[A, B, C, D] = [0, 0, 0, 1], Z = 1
