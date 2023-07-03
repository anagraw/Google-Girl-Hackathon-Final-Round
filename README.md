# Google_Girl_Hackathon_Final_Round
The problem statement for the Final Round was as follows: <br />
The task is to design an algorithm and write its code to identify the input vector required to identify the fault at a given node in a given circuit.
In a case, there would only be a single fault in the design.
The algorithm should be efficient, robust and able to identify faults quickly.

## <ins>Inputs</ins>

Available inputs are - <br />
&emsp;  1.Circuit file (format provided below) <br />
&emsp;  2.Fault node location <br />
&emsp;  3.Fault type <br />
&emsp; &emsp;   a)SA0 : stuck-at-0, a fault where node is not able to attain value 1, irrespective of inputs <br />
&emsp; &emsp;   b)SA1 : stuck-at-1, a fault where node is not able to attain value 0, irrespective of inputs <br />

## <ins>Outputs</ins> <br />
The code should print a vector for inputs to test the fault, and the expected value of output to confirm the fault.
The output should be printed to the following file in run directory - output.txt

## <ins>Circuit Format </ins>

  &emsp;1.The circuit will have 4 inputs - A, B, C and D. All of which are boolean type (only 0 and 1 are valid inputs) <br />
  &emsp;2.The circuit’s output will always be Z which is also a boolean. <br />
  &emsp;3.The circuit will be built using the following operations - <br />
    &emsp; &emsp;a)AND ( & ) gate <br />
    &emsp; &emsp;b)OR ( | ) gate <br />
    &emsp; &emsp;c)NOT ( ~ ) gate <br />
    &emsp; &emsp;d)XOR ( ^ ) gate <br />
  &emsp;4.The circuit would purely be a combinational logic. <br />
  &emsp;5.All internal nodes in the circuit would be named as : “net_<alphanumeric string>” <br />
  &emsp;6.Each input ( A / B / C / D ) would be utilized only once in the circuit. <br />

## <ins>Example Input </ins>

#### Circuit File: <br />
&emsp; net_e = A & B <br />
&emsp; net_f = C | D <br />
&emsp; net_g = ~ net_f <br />
&emsp; Z = net_g ^ net_e <br />

#### Fault: <br />
&emsp; FAULT_AT = net_f <br />
&emsp; FAULT_TYPE = SA0 <br />

## <ins> Example Output: </ins> <br />
[A, B, C, D] = [0, 0, 0, 1], Z = 1 <br />

## <ins>How to run the code: </ins>
&emsp;  1. You may clone the github repository using the git clone command in the terminal:  <br />
&emsp; &emsp; a) Navigate to the Code tab, and in the dropdown, choose HTTPS:  <br />
&emsp; &emsp; ![image](https://github.com/anagraw/Google_Girl_Hackathon_Final_Round/assets/92045291/929379b6-a5ff-49fc-afd5-f0b60c738206)  <br />
&emsp; &emsp; b) Open Git Bash  <br />
&emsp; &emsp; c) Change the current working directory to the location where you want the cloned directory.  <br />
&emsp; &emsp; d) Type git clone, and then paste the URL you copied earlier. <br />
&emsp; &emsp; ```
 git clone https://github.com/anagraw/Google_Girl_Hackathon_Final_Round.git
```


