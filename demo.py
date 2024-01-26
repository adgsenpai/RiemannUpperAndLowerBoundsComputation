from sympy import symbols, Sum, latex, simplify


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
&= \\sum_{{i=1}}^{{n}} \\left( -\\frac{{i}}{{n}} + 1 \\right) \\frac{{1}}{{n}} \\\\
&= -\\frac{{1}}{{n^2}} \\sum_{{i=1}}^{{n}} i + \\frac{{1}}{{n}} \\\\
&= -\\frac{{1}}{{n^2}} \\frac{{n(n+1)}}{{2}} + 1 \\\\
&= {latex(L_Pn_simplified)}
\\end{{align*}}

\\section*{{Upper Sum \( U(P_{{{n_val}}}) \)}}
For the Upper Sum \( U(P_{{{n_val}}}) \), we calculate the sum of the function values at the left endpoints of the subintervals times the width of each subinterval:
\\begin{{align*}}
U(P_{{{n_val}}}) &= {latex(U_Pn_expr)} \\\\
&= \\sum_{{i=1}}^{{n}} \\left( 1 - \\frac{{i-1}}{{n}} \\right) \\frac{{1}}{{n}} \\\\
&= \\frac{{1}}{{n^2}} \\sum_{{i=1}}^{{n}} (n-i+1) \\\\
&= \\frac{{1}}{{n^2}} \\left(n^2 + n - \\frac{{n(n-1)}}{{2}}\\right) \\\\
&= {latex(U_Pn_simplified)}
\\end{{align*}}

\\end{{document}}
    """
    
    return latex_code

# Generate LaTeX code with all steps and function values
# Define the function f(x) = -x + 1
x = symbols('x')
f_x = -x + 1
n_val = symbols('n')  # Use a symbolic value for n

# Generate LaTeX code with all steps
latex_output_with_steps = calculate_sums_with_steps(f_x, n_val)
print(latex_output_with_steps)
