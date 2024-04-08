# State Class
* Class 
  * attributes: 
    * isTerminating -> boolean
    * isInitial -> boolean
    * map of transitions
      * key -> symbol 
      * value -> list of state
* We should have a map containing all the existing states.
* at each state we know the current character.