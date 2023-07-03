# Google_Girl_Hackathon_Final_Round
The problem statement for the Final Round was as follows:
The task is to design an algorithm and write its code to identify the input vector required to identify the fault at a given node in a given circuit.
In a case, there would only be a single fault in the design.
The algorithm should be efficient, robust and able to identify faults quickly.

<ins>Inputs</ins>

Available inputs are -
  1.Circuit file (format provided below) <br />
  2.Fault node location <br />
  3.Fault type <br />
    a)SA0 : stuck-at-0, a fault where node is not able to attain value 1, irrespective of inputs <br />
    b)SA1 : stuck-at-1, a fault where node is not able to attain value 0, irrespective of inputs <br />
<ins>Outputs</ins>
The code should print a vector for inputs to test the fault, and the expected value of output to confirm the fault.
The output should be printed to the following file in run directory - output.txt

<ins>Circuit Format </ins>

  1.The circuit will have 4 inputs - A, B, C and D. All of which are boolean type (only 0 and 1 are valid inputs) <br />
  2.The circuit’s output will always be Z which is also a boolean. <br />
  3.The circuit will be built using the following operations - <br />
    a)AND ( & ) gate <br />
    b)OR ( | ) gate <br />
    c)NOT ( ~ ) gate <br />
    d)XOR ( ^ ) gate <br />
  4.The circuit would purely be a combinational logic. <br />
  5.All internal nodes in the circuit would be named as : “net_<alphanumeric string>” <br />
  6.Each input ( A / B / C / D ) would be utilized only once in the circuit. <br />

<ins>Example Input </ins>

Circuit File: <br />
net_e = A & B <br />
net_f = C | D <br />
net_g = ~ net_f <br />
Z = net_g ^ net_e <br />

Fault: <br />
FAULT_AT = net_f <br />
FAULT_TYPE = SA0 <br />

Example Output: <br />
[A, B, C, D] = [0, 0, 0, 1], Z = 1 <br />
