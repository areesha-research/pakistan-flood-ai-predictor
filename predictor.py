import pandas as pd
import io
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# 1. Broad regional data blocks perfectly aligning with your paper's text
csv_data = """Region,Rainfall_mm,Water_Stagnation_Days,Flood_Status
Nowshera (KPK),390,4,Moderate
Sindh Region,510,9,Critical
Punjab Region,280,2,Low"""

df = pd.read_csv(io.StringIO(csv_data))

# 2. Public health risk classifier logic
def predict_epidemic_risk(row):
    if row['Flood_Status'] == 'Critical' or row['Water_Stagnation_Days'] > 5:
        return 'HIGH RISK (Immediate Intervention Required)'
    elif row['Water_Stagnation_Days'] > 2:
        return 'MEDIUM RISK (Monitor Closely)'
    else:
        return 'LOW RISK'

df['Epidemic_Threat_Level'] = df.apply(predict_epidemic_risk, axis=1)

# 3. Direct color mapping
color_map = {
    'HIGH RISK (Immediate Intervention Required)': '#e63946', 
    'MEDIUM RISK (Monitor Closely)': '#f4a261', 
    'LOW RISK': '#2a9d8f'
}
bar_colors = df['Epidemic_Threat_Level'].map(color_map).tolist()

# 4. Generate the optimized chart layout
plt.figure(figsize=(8, 5))
plt.bar(df['Region'], df['Water_Stagnation_Days'], color=bar_colors, edgecolor='black', width=0.45)

# 5. Academic titles matching your exact title layout
plt.title('Post-Flood Epidemic Risk Analysis: Case Studies from Pakistan', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Analyzed Regional Study Zones', fontsize=10, labelpad=10)
plt.ylabel('Days of Continuous Water Stagnation', fontsize=10, labelpad=10)
plt.grid(axis='y', linestyle='--', alpha=0.4)

# 6. Build legend dynamically
legend_elements = list()
legend_elements.append(Patch(facecolor='#e63946', edgecolor='black', label='High Outbreak Risk'))
legend_elements.append(Patch(facecolor='#f4a261', edgecolor='black', label='Medium Outbreak Risk'))
legend_elements.append(Patch(facecolor='#2a9d8f', edgecolor='black', label='Low Outbreak Risk'))
plt.legend(handles=legend_elements, title='AI Predicted Vector Threat', loc='upper right', fontsize=9)
plt.tight_layout()

# 7. Save file explicitly for your manuscript
plt.savefig('pakistan_regional_epidemic_risk_chart.png', dpi=300)
print("Success! Your final regional chart has been saved.")
