from flask import Flask, render_template, request
import sympy as sp
import math

app = Flask(__name__)

def solve_percentage_problem(initial_value, percentage_change, years, increase=True):
    steps = []
    final_value = initial_value
    factor = (1 + percentage_change / 100) if increase else (1 - percentage_change / 100)
    
    steps.append(f"Initial value: {initial_value}")
    steps.append(f"Each year's {'increase' if increase else 'decrease'} factor: {factor}")
    
    for year in range(1, years + 1):
        final_value *= factor
        steps.append(f"After year {year}: {final_value:.2f}")
    
    result = f"Final value after {years} years: {final_value:.2f}"
    steps.append(result)
    
    return "<br>".join(steps)

def calculate_lcm_hcf(a, b):
    lcm = math.lcm(a, b)
    hcf = math.gcd(a, b)
    return f"LCM of {a} and {b} is {lcm}<br>HCF of {a} and {b} is {hcf}"

def calculate_profit_loss(cost_price, selling_price):
    if selling_price > cost_price:
        profit = selling_price - cost_price
        percentage = (profit / cost_price) * 100
        return f"Profit: {profit}<br>Profit Percentage: {percentage:.2f}%"
    else:
        loss = cost_price - selling_price
        percentage = (loss / cost_price) * 100
        return f"Loss: {loss}<br>Loss Percentage: {percentage:.2f}%"

def calculate_compound_interest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    return f"Compound Interest: {ci:.2f}<br>Final Amount: {amount:.2f}"

def calculate_ratio_proportion(a, b, c):
    d = (b * c) / a
    return f"Ratio Proportion Result: {a}:{b} = {c}:{d:.2f}"

def solve_quadratic(a, b, c):
    x = sp.symbols('x')
    eq = a*x**2 + b*x + c
    solutions = sp.solve(eq, x)
    return f"Solutions for {eq} are: {solutions}"

def find_prime_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        while (n % i) == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return f"Prime factors of {n} are: {factors}"

@app.route('/', methods=['GET', 'POST'])
def index():
    solution = ""
    if request.method == 'POST':
        math_type = request.form.get('math_type', '')
        
        try:
            if math_type == 'percentage':
                initial_value = float(request.form.get('initial_value', 0))
                percentage_change = float(request.form.get('percentage_change', 0))
                years = int(request.form.get('years', 0))
                increase = request.form.get('increase', 'True') == 'True'
                solution = solve_percentage_problem(initial_value, percentage_change, years, increase)
            
            elif math_type == 'lcm_hcf':
                a = int(request.form.get('num1', 0))
                b = int(request.form.get('num2', 0))
                solution = calculate_lcm_hcf(a, b)
            
            elif math_type == 'profit_loss':
                cost_price = float(request.form.get('cost_price', 0))
                selling_price = float(request.form.get('selling_price', 0))
                solution = calculate_profit_loss(cost_price, selling_price)
            
            elif math_type == 'compound_interest':
                principal = float(request.form.get('principal', 0))
                rate = float(request.form.get('rate', 0))
                time = int(request.form.get('time', 0))
                solution = calculate_compound_interest(principal, rate, time)
            
            elif math_type == 'ratio_proportion':
                a = float(request.form.get('a', 0))
                b = float(request.form.get('b', 0))
                c = float(request.form.get('c', 0))
                solution = calculate_ratio_proportion(a, b, c)
            
            elif math_type == 'quadratic':
                a = float(request.form.get('quad_a', 0))
                b = float(request.form.get('quad_b', 0))
                c = float(request.form.get('quad_c', 0))
                solution = solve_quadratic(a, b, c)
            
            elif math_type == 'prime_factors':
                n = int(request.form.get('prime_n', 0))
                solution = find_prime_factors(n)
        
        except ValueError:
            solution = "Invalid input. Please enter valid numbers."
        
    return render_template('index.html', solution=solution)

if __name__ == '__main__':
    app.run(debug=True)
