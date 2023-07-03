# Google Girl Hackathon Final Round

## <ins>Problem Statement</ins> <br />

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
&emsp; You may clone the GitHub repository using the git clone command in the terminal:  <br />
&emsp; &emsp; a) Navigate to the Code tab, and in the dropdown, choose HTTPS:  <br />
&emsp; &emsp; ![image](https://github.com/anagraw/Google_Girl_Hackathon_Final_Round/assets/92045291/929379b6-a5ff-49fc-afd5-f0b60c738206)  <br />
&emsp; &emsp; b) Open Git Bash  <br />
&emsp; &emsp; c) Change the current working directory to the location where you want the cloned directory.  <br />
&emsp; &emsp; d) Type git clone, and then paste the URL you copied earlier. <br />
&emsp; &emsp; &emsp;  ```git clone https://github.com/anagraw/Google_Girl_Hackathon_Final_Round.git ```

## ***I Will Always Try To Find You*** <br />

Sounds like a horror story title? Well, it is! <br />
The program haunts the stuck-at faults present in the circuit! <br />
The program finds the input vector to detect Stuck at Fault in a Circuit Net and also returns the output value Z as well, which helps to confirm the fault.<br /> 

## Things you need to know:
&emsp; * The submission.py file has the main program that returns the input vector to detect the stuck-at-fault. <br />
&emsp; * The input.txt file contains the circuit file. <br />
&emsp; * The fault.txt file contains the fault present in the circuit in the required format. <br />
&emsp; * The program generates a dummy value of Z and an empty list if there is no valid input test combination <br />
&emsp; * The output.txt is the file containing the input vector and Z value required to detect the fault. <br />
&emsp;     (This file is generated upon executing the program) <br />

## Few Requirements for the circuit file and fault file:
&emsp; * The Circuit file should strictly have 4 inputs: A,B,C and D respectively only. <br />
&emsp; * The Fault file should strictly contain only one stuck at fault. <br />
&emsp; * The nets in the Circuit file should be named net_e, net_f and net_g respectively only. <br />
&emsp; * The output in the Circuit file should be strictly named Z only. <br />


## How is this program an optimized approach:
Let us say we have a server that can handle 10^8 operations per second, and hypothetically we have 20 inputs <br />
Using the conventional approach of testing a combination of 0s and 1s as input <br />
The program runs in 10 milliseconds <br />
With our PODEM algorithm, the program runs in 20 microseconds <br />
As the number of inputs increases from 20 to 50, the traditional 2^N algorithm takes several minutes while the <br />
PODEM algorithm runs it in seconds <br />


## Future ideas to enhance the project and delve deeper:
&emsp;1. Solve for circuits with a greater number of inputs and automate the process for n number of input gates. <br />
&emsp;2. Research on faster approaches with time complexity less than O(N) where N is the number of input gates. <br />
&emsp;   Faster approaches will help solve more complex circuits easily. <br />
&emsp;&emsp; Currently using the PODEM algorithm significantly reduces the time complexity from O(2^N) to O(N), <br />
&emsp;&emsp; We can look for better algorithms that take lesser time  <br />
&emsp;3. Create a web app to show circuit simulations and make the experience more interactive. <br />





<ins> Note:- In the future, changes might be made to make the program foolproof </ins>
<ins> and incorporate corner cases or suggestions if found. </ins> <br />
<ins> Replication of the program for publishing purposes without prior permission is not allowed</ins> <br />

