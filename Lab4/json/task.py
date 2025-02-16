import json as js

data = js.load("sample-data.json", 'r')


print("Interface Status")
print("=" * 80)
print(f"{'DN':<30} {'Description':<20} {'Speed':<7} {'MTU':<5}")
print("-" * 80)

interface = data['imdata']
print(interface)

for i in interface:
    dn = interface.get("dn", "none")