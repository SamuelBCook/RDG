# RDG
## _Random Data Generator_

RDG is a simple (pseudo) random data generator. It is aimed at Data Scientists, Engineers, and Analysts, with ease of use the priority. It contains the following functions:  

- rand_bool
- rand_float
- rand_int
- rand_text
- rand_choice

Each returns a generator containing the desired data type(s). For each method, the only parameter required is 'num_rows', which is the length of the generator. 


## Methods

> Run 'python3 -m randdg -help' to see a list of methods

### __rand_bool__
 > Creates a generator containing only bools.

___class RDG.rand_bool(num_rows, true_frac=0.5, false_frac=0.5)___ 

- __num_rows__: (int) the length of the generator.
- __true_frac__: (float) the fraction of True bools desired. Defaults to 0.5.
- __false_frac__: (float) the fraction of False bools desired. Defaults to 0.5. 

### __rand_float__ 
> Creates a generator containing only floats in the given range. 

___class RDG.rand_float(num_rows, min_float=0, max_float=20, decimals=2)___ 

- __num_rows__: (int) the length of the generator.
- __min_float__: (float or int) minimum of range of floats desired. Defaults to 0.
- __max_float__: (float or int) maximum of range of floats desired. Defaults to 20.
- __decimals__: (int) number of decimals to round to. Defaults to 2. 

### __rand_int__ 
> Creates a generator containing only integers in the given range. 

___class RDG.rand_int(num_rows, min_int=0, max_int=100)___ 
- __num_rows__: (int) the length of the generator.
- __min_int__: (int) the minimum of the range of integers desired. Defaults to 0.
- __max_int__: (int)  the maximum of the range of integers desired. Defaults to 100.

### __rand_text__ 
> Creates a generator containing random strings split into x number of words. 

___class RDG.rand_text(num_rows, min_ltrs=6, max_ltrs=14, num_words=3, capitalise=True, strip=True)___ 
- __num_rows__: (int) the length of the generator.
- __min_ltrs__: (int) minimum number of characters desired (not including white space). Defaults to 6.
- __max_ltrs__: (int) maximum number of characters desired (not including white space). Defaults to 14.
- __num_words__: (int) number of words desired. Defaults to 2.
- __capitalise__: (bool) whether to make the word(s) title case. Defaults to False. 
- __strip__: (bool) whether to strip leading and trailing whitespace. Defaults to True.

### __rand_choice__ 
> Creates a generator using only values passed to the  method.

___class RDG.rand_choice(num_rows, values)___ 
- __num_rows__: (int) the length of the generator.
- __values__: (list) a list of values to choose from for the generator. 

## Other
- GitHub Repository: [RDG](https://github.com/SamuelBCook/RDG)
