#Scope 3 Category 1 Emissions Calculator # Spend-Based Method
import matplotlib.pyplot as plt
# Scope 1
diesel_litres = 5000
diesel_emission_factor = 2.68      #kg CO2e per diesel_litres
scope1 = diesel_litres * diesel_emission_factor
# Scope 2
electricity_kwh = 30000
india_grid_factor = 0.82
scope2 = electricity_kwh * india_grid_factor

category_spend = {
    "Purchased Steel": 1000000,
    "Aluminium": 500000,
    "Office Supplies": 100000,
    "Business Travel": 250000,
    "IT Consulting": 150000
}
emission_factor = 0.0005
scope3 = 0
for category, spend in category_spend.items():

    emissions_kg = spend * emission_factor
    emissions_tonnes = emissions_kg / 1000

    print(f"\nCategory: {category}")
    print(f"Spend (INR): {spend:,.2f}")
    print(f"Emission Factor: {emission_factor}")
    print(f"Emissions (kg CO2e): {emissions_kg:,.2f}")
    print(f"Emissions (tonnes CO2e): {emissions_tonnes:.3f}")

    scope3 += emissions_kg
    grand_total = scope1 + scope2 + scope3
    scope1_percent = (scope1 / grand_total) * 100
    scope2_percent = (scope2 / grand_total) * 100
    scope3_percent = (scope3 / grand_total) * 100
print("\n==============================")
print("Corporate Emissions Summary")
print("==============================")

print(f"Scope 1 : {scope1:.2f} kg CO2e")
print(f"Scope 2 : {scope2:.2f} kg CO2e")
print(f"Scope 3 : {scope3:.2f} kg CO2e")

print("------------------------------")

print(f"Grand Total : {grand_total:.2f} kg CO2e")

print("\nPercentage Contribution")

print(f"Scope 1 : {scope1_percent:.1f}%")
print(f"Scope 2 : {scope2_percent:.1f}%")
print(f"Scope 3 : {scope3_percent:.1f}%")
scopes = ["Scope 1", "Scope 2", "Scope 3"]

values = [scope1, scope2, scope3]

plt.bar(scopes, values)

plt.title("Corporate Greenhouse Gas Emissions")

plt.xlabel("Emission Scopes")

plt.ylabel("kg CO2e")

plt.savefig("scope_emissions_chart.png")

plt.show()