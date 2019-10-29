# A simple command-line Boggle-inspired word game implemented in Python.

### Features:

1. Gets an input from the user
2. Searches for the existence of that input in a 4x4 board
3. Validates if the word input by the user is a valid word in the dictionary

### Implementations:

1. Backtracking algorithm to search for the word in the board
2. Binary search algorithm to search for the word in the dictionary

#### Learning points:

1. Writing documentation (I followed Google's [pyguide](http://google.github.io/styleguide/pyguide.html))

   ```py
   """ Short description.

   More detailed description and explanation here.

   Args:
       args_1 : A str representing an argument
       args_2 : An int representing another argument

   Returns:
       A list containing some information
   """
   ```

2. Organising and modularising code.  
   This time I separated my code according to the functions they serve, e.g., all dictionary-related logic, such as loading and searching the dictionary, went into `boggle_dictionary.py`.
   I also put all my reusable logic in separate functions and modules, imported them in the main file, called them accordingly in a function named `main()`, and finally called it inside the `if __name__ == '__main__':` block.
3. Timing my code to evaluate its performance.  
   Using `timeit`, I measured the time taken to load an almost 300,000-line-long .txt file. While I did not do anything to improve the loading performance, I feel like this is my first step towards learning how to optimise my code.
