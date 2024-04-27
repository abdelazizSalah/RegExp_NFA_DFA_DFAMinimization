# Regex to NFA to DFa to minimized DFA

* In this project we have implemented a command line tool which takes as an input a regular expression (Regex), and then shows its:
  1. NFA
  2. DFA
  3. Minimized DFA

* The flow of the project was as follow:
    1. reading the regex as a string
    2. validating the regex
    3. implementing a Lexer to make the parsing more efficient and easier
    4. implementing a Regex Parser using Recursive descent algorithm after defining our grammar
    5. Then converting the recursive descent to postfix string, to be able to apply the Shunting yard algorithm 
    6. Converting the postfix string into NFA using the Shunting yard algorithm and Thompson's algorithm
    7. Converting the NFA to DFA using the Subset Algorithm
    8. Then using dynamic programming (DP) to get the minimized DFA

> check the notebook, it contains the hand analysis images, and the source code of the solution, and feel free to test it, there is a testing cell at the end of the notebook you can test it from there 🫡💓

## Samples of output
* Regex = 'zizo|(z(u|o)z)' => my nickname btw 😉
  ![my nickname](https://github.com/abdelazizSalah/RegExp_NFA_DFA_DFAMinimization/assets/71516308/0f32bff0-2b29-4487-add9-0d362ed8cbe0)
* Regex = '(7|h|H)osny' => my fellow nickname 💓🫡
  ![image](https://github.com/abdelazizSalah/RegExp_NFA_DFA_DFAMinimization/assets/71516308/907aaf38-7dca-4b14-9701-6ed2ae49cd1c)
* Regex = '((bashohandes)|(Eng)|TA)(3|O|o)mar (S|s)amir we are done+' => our TA name with his title => to get the grades 😂
  ![image](https://github.com/abdelazizSalah/RegExp_NFA_DFA_DFAMinimization/assets/71516308/ec48b9fc-9769-4c31-aa2a-40a240c95356)
* Regex = "(a|b)zi+
  ![image](https://github.com/abdelazizSalah/RegExp_NFA_DFA_DFAMinimization/assets/71516308/3ae7d6f6-d4b5-4217-a460-502c6bcd81bd)




  
