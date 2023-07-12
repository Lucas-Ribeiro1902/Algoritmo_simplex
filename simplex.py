import tkinter as tk
from scipy.optimize import linprog

def solve_lp_problem(c, A, b):
    # Using the linprog function from scipy to solve the linear programming problem
    res = linprog(c, A_ub=A, b_ub=b, method='simplex')
    return res.x, res.fun

def solve_problem():
    # Obtain the values of the objective function coefficients and constraints
    c = [float(c_entry.get()) for c_entry in c_entries]
    A = [[float(A_entries[i][j].get()) for j in range(num_variables)] for i in range(num_constraints)]
    b = [float(b_entry.get()) for b_entry in b_entries]

    # Solve the problem using the simplex method
    solution, optimal_value = solve_lp_problem(c, A, b)

    # Display the solution and optimal value
    solution_label.config(text=f"Solução: {solution}")
    optimal_value_label.config(text=f"Valor ótimo: {optimal_value}")


# Create the main window
window = tk.Tk()
window.title("symplex PY")

# Create the entries for the objective function coefficients
num_variables = 3  # Number of variables in the objective function
c_entries = []
for i in range(num_variables):
    c_label = tk.Label(window, text=f"c[{i+1}]:")
    c_label.grid(row=i, column=0, padx=5, pady=5, sticky="E")
    c_entry = tk.Entry(window)
    c_entry.grid(row=i, column=1, padx=5, pady=5, sticky="W")
    c_entries.append(c_entry)

# Create the entries for the constraint coefficients
num_constraints = 3  # Number of constraints
A_entries = []
b_entries = []
for i in range(num_constraints):
    A_entries.append([])
    for j in range(num_variables):
        A_label = tk.Label(window, text=f"A[{i+1}][{j+1}]:")
        A_label.grid(row=i+num_variables, column=j, padx=5, pady=5, sticky="E")
        A_entry = tk.Entry(window)
        A_entry.grid(row=i+num_variables, column=j+1, padx=5, pady=5, sticky="W")
        A_entries[i].append(A_entry)
    b_label = tk.Label(window, text=f"b[{i+1}]:")
    b_label.grid(row=i+num_variables, column=num_variables+1, padx=5, pady=5, sticky="E")
    b_entry = tk.Entry(window)
    b_entry.grid(row=i+num_variables, column=num_variables+2, padx=5, pady=5, sticky="W")
    b_entries.append(b_entry)

# Button to solve the problem
solve_button = tk.Button(window, text="Resolver", command=solve_problem)
solve_button.grid(row=num_variables+num_constraints, column=0, columnspan=num_variables+3, padx=5, pady=10)

# Labels to display the solution and optimal value
solution_label = tk.Label(window, text="Solução:")
solution_label.grid(row=num_variables+num_constraints+1, column=0, columnspan=num_variables+3, padx=5, pady=5)
optimal_value_label = tk.Label(window, text="Valor ótimo:")
optimal_value_label.grid(row=num_variables+num_constraints+2, column=0, columnspan=num_variables+3, padx=5, pady=5)

# Start the main window loop
window.mainloop()
