# Email: 23f3003731@ds.study.iitm.ac.in

# =========================
# Cell 1: Load and prepare data
# =========================
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    "x": range(1, 101),
    "y": [v**2 for v in range(1, 101)]  # y depends on x
})

# Display first few rows
data.head()

# =========================
# Cell 2: Interactive slider and dynamic markdown
# =========================
import marimo as mo

# Slider to select number of points to display
slider = mo.ui.slider(1, 100, value=10)

# Dynamic markdown that updates based on slider
mo.md(f"Displaying **{slider.value}** points: 🟢" * slider.value)

# Slice data based on slider value
displayed_data = data.iloc[:slider.value]
displayed_data
