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