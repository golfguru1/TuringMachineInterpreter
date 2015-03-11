# Turing Machine Interpreter

This is a universal turing machine interpreter. It takes input from a text file in the form of:

Lines beginning with `t` are the instructions for the Turing Machine

```
t currentState inputSymbol nextState writeSymbol headMoveDirection
```

Lines beginning with `i` are the inputs to the Turing Machine

```
i 01111001
```

Lines beginning with `f` are the final accepting states of the Turing Machine

```
f 2 3
```

It will output the modified input string as well as whether or not it was accepted by the Turing Machine
##Installation

The interpreter is run from the command line:

	python < inputFile.txt
