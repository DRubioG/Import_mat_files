# Import_mat_files
 This repository includes the Python function to import a .mat file(Matlab) to Python like it was a Python  variable

# Watch out
This function only works if it is in the file you want to use. If you want to export a variable, you need to call in a file an rename the variable.
For a better use copy-paste from this file.

This function creates like Matlab a variable with value if only has one value, and a list if it has more than one value

## First option -> load()
Like Matlab

``` python
def load(file, *args):
    '''
    This function loads .mat files to Python like Python variables.
    Input:
        - file : the .mat file you want to load. Doesn't matter if ends in '.mat' or not.
        - specific_variables : this options load only specific variables from .mat file.
    '''

    if file[-4:] != ".mat":
        file += ".mat"

    import scipy.io
    mat = scipy.io.loadmat(file)
    for k,_ in mat.items():
        if k != "__header__" and k != "__globals__" and k != "__version__":

            # specific variable
            if len(args) != 0:
                for i in args:
                    if i == k:
                        if mat.get(k).shape[0] == 1:        # when list has only a row
                            if mat.get(k).shape[1] == 1:    # when object has one value
                                globals()[f"{k}"] = mat.get(k)[0][0].tolist()
                            else:
                                globals()[f"{k}"] = mat.get(k)[0].tolist()
                        else:
                            globals()[f"{k}"] = mat.get(k).tolist()
                        
            else:
                # non-specific variable
                if mat.get(k).shape[0] == 1:
                    if mat.get(k).shape[1] == 1:
                        globals()[f"{k}"] = mat.get(k)[0][0].tolist()
                    else:
                        globals()[f"{k}"] = mat.get(k)[0].tolist()
                else:
                    globals()[f"{k}"] = mat.get(k).tolist()

load("matlab_file.mat", "first_variable")
print(first_variable)
load("matlab_file2")

```

## Second option -> load_var()
Like Matlab but with the option to watch the variables

``` python
def load_var(file, printvar='off', *args):
    '''
    This function loads .mat files to Python like Python variables, and print the names of
    the import variables.
    Input:
        - file : the .mat file you want to load. Doesn't matter if ends in '.mat' or not.
        - printvar : this option prints the name of new variable. Two options:
                    - 'on'  : it prints the name
                    - 'off' : it doesn't print the name
        - specific_variables : this options load only specific variables from .mat file.
    '''

    if file[-4:] != ".mat":
        file += ".mat"

    import scipy.io
    mat = scipy.io.loadmat(file)
    for k,_ in mat.items():
        if k != "__header__" and k != "__globals__" and k != "__version__":

            # specific variable
            if len(args) != 0:
                for i in args:
                    if i == k:
                        if mat.get(k).shape[0] == 1:        # when list has only a row
                            if mat.get(k).shape[1] == 1:    # when object has one value
                                globals()[f"{k}"] = mat.get(k)[0][0].tolist()
                            else:
                                globals()[f"{k}"] = mat.get(k)[0].tolist()
                        else:
                            globals()[f"{k}"] = mat.get(k).tolist()
                        
            else:
                # non-specific variable
                if mat.get(k).shape[0] == 1:
                    if mat.get(k).shape[1] == 1:
                        globals()[f"{k}"] = mat.get(k)[0][0].tolist()
                    else:
                        globals()[f"{k}"] = mat.get(k)[0].tolist()
                else:
                    globals()[f"{k}"] = mat.get(k).tolist()
            
            if printvar=='on':
                print(k)

load_var("matlab_file.mat", 'off', "first_variable")
print(first_variable)
load_var("matlab_file2", 'on')

```