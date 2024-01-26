from sympy import symbols, Sum, latex, simplify, limit, oo

# Update the function to include the calculation of mi and m_hat_i, and their LaTeX representations
def calculate_sums_with_steps_and_values(f_x, n_val):
    x, i = symbols('x i')
    delta_x = 1/n_val
    
    # Values of f at the right endpoints (mi) and left endpoints (m_hat_i)
    mi = f_x.subs(x, i/n_val)
    m_hat_i = f_x.subs(x, (i-1)/n_val)
    
    # Lower Sum L(Pn): Use the right endpoints of the subintervals (i/n)
    L_Pn_expr = Sum(mi * delta_x, (i, 1, n_val))
    L_Pn_simplified = simplify(L_Pn_expr.doit())
    
    # Upper Sum U(Pn): Use the left endpoints of the subintervals ((i-1)/n)
    U_Pn_expr = Sum(m_hat_i * delta_x, (i, 1, n_val))
    U_Pn_simplified = simplify(U_Pn_expr.doit())

    # Calculate the limit as n approaches infinity for both sums
    L_Pn_limit = limit(L_Pn_simplified, n_val, oo)
    U_Pn_limit = limit(U_Pn_simplified, n_val, oo)

    # Generate the LaTeX code with all steps
    latex_code = f"""
\\documentclass{{article}}
\\usepackage{{amsmath}}
\\begin{{document}}

\\section*{{Function Values}}
The function values at the right endpoints (for the lower sum) and at the left endpoints (for the upper sum) are given by:
\\begin{{align*}}
m_i &= f\\left(\\frac{{i}}{{n}}\\right) = {latex(mi)} \\\\
\\hat{{m}}_i &= f\\left(\\frac{{i-1}}{{n}}\\right) = {latex(m_hat_i)}
\\end{{align*}}

\\section*{{Lower Sum \( L(P_{{{n_val}}}) \)}}
For the Lower Sum \( L(P_{{{n_val}}}) \), we calculate the sum of the function values at the right endpoints of the subintervals times the width of each subinterval:
\\begin{{align*}}
L(P_{{{n_val}}}) &= {latex(L_Pn_expr)} \\\\
&= {latex(L_Pn_simplified)} \\\\
\\text{{Limit as }} n \\to \\infty: \\lim_{{n\\to\\infty}} L(P_n) &= {latex(L_Pn_limit)}
\\end{{align*}}

\\section*{{Upper Sum \( U(P_{{{n_val}}}) \)}}
For the Upper Sum \( U(P_{{{n_val}}}) \), we calculate the sum of the function values at the left endpoints of the subintervals times the width of each subinterval:
\\begin{{align*}}
U(P_{{{n_val}}}) &= {latex(U_Pn_expr)} \\\\
&= {latex(U_Pn_simplified)} \\\\
\\text{{Limit as }} n \\to \\infty: \\lim_{{n\\to\\infty}} U(P_n) &= {latex(U_Pn_limit)}
\\end{{align*}}

\\end{{document}}
    """
    
    # Check if the function is Riemann integrable by comparing the limits
    is_riemann_integrable = L_Pn_limit == U_Pn_limit

    return latex_code, is_riemann_integrable

# Generate LaTeX code with all steps and function values
# Define the function f(x) = -x + 1
x = symbols('x')
f_x = -x + 1
n_val = symbols('n')  # Use a symbolic value for n

# Generate LaTeX code with all steps
latex_output_with_steps, is_riemann_integrable = calculate_sums_with_steps_and_values(f_x, n_val)

# Print LaTeX code and whether the function is Riemann integrable
print(latex_output_with_steps)
print(f"Is the function Riemann integrable? {is_riemann_integrable}")
