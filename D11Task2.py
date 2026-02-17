import matplotlib.pyplot as plt

# Data for bar chart
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Data for line plot (example: monthly sales trend)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
monthly_sales = [500, 600, 550, 650, 700]

# Create figure

# --- Subplot 1: Bar Chart ---
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Product Category")
plt.ylabel("Sales")

# --- Subplot 2: Line Plot ---
plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the dashboard
plt.show()
