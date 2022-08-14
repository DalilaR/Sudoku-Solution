assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)
#For diagonal Suduko
#Create the 2 diagonals
#Add them to the right units, then and only then, update peers
diagonal_units = [[''.join([v,t])for v,t in zip(rows,cols)],[''.join([v,t]) for v,t in zip(f,cols)]]
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values
def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
#Get a value in the grid.  Make sure that the value as at least 2 digits.
#Find its its units
#In each unit, check if a duplicate exists, if it does go over the unit and replace the its digits
# from all the other boxes.
    k_keys = []
    mydict = { k:v for k,v in values.items() if len(v) > 1 }
    for i in mydict:
        if len(values[i]) == 2:
            for k in units[i]:
                k_keys = list(k)
                solved_values = set()
                solved_values = [box for box in k if values[box] == values[i]]
                if len(solved_values) > 1:
                    for digit in values[i]:
                        for j in k:
                            if  j not in solved_values and digit in values[j]:
                                new_val = values[j]
                                new_val = new_val.replace(digit,'')
                                values = assign_value(values,j,new_val)
    return (values) 
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers

def cross(A, B):
    "Cross product of elements in A and elements in B."
     return [s+t for s in a for t in b]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))
def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
      I just copied from you
    """
     width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    print
    pass

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

"""
To solve the problem of unique_choice.
Go over all the units (81) 
The algorithm:
create a dictionary of location by digit.
The keys represent the digits, values are a list of locations
Go through the dictionary and find which one has only one entry or one location
That location implies unique value for the digit.
Now, assign the value in that key location to the location in values
"""
"""
Developed my own function.  The code is longer than the one provided by the course, but it creates a dictionary 
where the digits are the keys and the values are a list of locations.  If a key has only one value, then the 
value is unique
"""
def only_choice(values):
       tmp_dict = values
    tmp_dict2 = {}
    for l in values:
        for m in units[l]:
            tmp_dict2 = tmp_dict2.fromkeys(m)
            st = '123456789'
            unique_value = {}
            unique_v = list(st)
            unique_value = unique_value.fromkeys(unique_v)
            for i in m:
                if len(tmp_dict[i]) == 1:
                    unique_value[tmp_dict[i]] = i
                    del tmp_dict2[i]
                else:
                    tmp_dict2[i] = tmp_dict[i]
            mydict = { k:v for k,v in unique_value.items() if v!=None }
            unique_value = mydict
            #Make sure that none of the unique values are in the sets
            for i in unique_value:
                for k in tmp_dict2:
                    tmp_dict2[k] = tmp_dict2[k].replace(i,'')
                    tmp_dict[k] = tmp_dict2[k]
#Now that we know that we don't have copies of unique values
# we can just create a dictionary based on the numbers and 
# put the locations in them.  If the number maps to one location
# we are done
            tmp_key = list(tmp_dict2.keys())
            tmp_value = list(tmp_dict2.values())
            unique_v = list(st)
            find_unique = {}
            find_unique = find_unique.fromkeys(unique_v,[])
            l = len(tmp_value)
            for i in range(0,l):
                t = list(tmp_value[i])
                for k in t:
                    p = [tmp_key[i]]
                    find_unique[k] = find_unique[k]+p
            for i in find_unique:
                if len(find_unique[i]) == 1:
                    x = find_unique[i][0]
                    values = assign_value(tmp_dict,x, i)
    return values

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
     values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    """Add to the 2 diagonals to their respective units, and peers.  Also update unitlist to contain the 
    the 2 diagonals.  No other changes are needed.
    """
    for i in diagonal_units:
        for k in i:
            if i not in units[k]:
                units[k] = [units[k]+[i]][0]
    #Now update peers to have values from diagonal        
    for i in diagonal_units:
        for k in i:
         x = set(i)
            peers[k] = peers[k].union(x)
    unitlist = row_units + column_units + square_units+diagonal_units
    #Create values from the grid
    values = grid_values(new_grid)
    values = search(values)
    return (values)
if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
