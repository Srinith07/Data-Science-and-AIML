contacts = {"Darshan": 9731629259, "Utsav": 9731629258,
            "Satyarth": 9731629257, "Shivam": 9731629256}
contacts["Ram"] = 9731629255
contacts.pop("Satyarth")
contact_shivam = contacts.get("Shivam")
contact_satyarth = contacts.get("Satyarth", "Contact not found")
contacts.items()
print(contact_satyarth)
print(contact_shivam)
print(contacts)
