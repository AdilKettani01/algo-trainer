import big_o
from big_o.reports import big_o_report
def return_first_elemnt(lst):
    """
    This function takes a list as input and returns the first element of the list.
    
    Parameters:
    lst (list): A list of elements.
    
    Returns:
    The first element of the list if the list is not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None


data_generator = lambda n: big_o.datagen.integers(n, 1, 1000)

best_fit, fitted_complexity = big_o.big_o(return_first_elemnt, data_generator, min_n=10, max_n=1000, n_measures=10)

print(f"Best fit complexity: {best_fit}")
print(big_o_report(best_fit, fitted_complexity))