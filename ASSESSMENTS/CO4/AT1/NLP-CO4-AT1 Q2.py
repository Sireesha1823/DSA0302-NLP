machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

print("Machine Status:")
for machine, status in machines.items():
    print(machine, "->", status)

print("\nDerived Predicates:")

for machine, status in machines.items():

    if status == "Active":
        print("Active(" + machine + ")")
        print("Producing(" + machine + ")")

    elif status == "Maintenance":
        print("Maintenance(" + machine + ")")
        print("NOT Producing(" + machine + ")")
