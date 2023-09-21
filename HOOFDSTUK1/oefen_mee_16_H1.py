landen_feiten = {
    'Frankrijk': {
        'hoofdstad': 'Parijs',
        'bevolking': 67348000,
        'taal': 'Frans',
    },
    'België': {
        'hoofdstad': 'Brussel',
        'bevolking': 11563000,
        'taal': ['Nederlands', 'Frans', 'Duits'],
    },
    'Duitsland': {
        'bevolking': 83190556,
        'taal': 'Duits',
    }
}

print("Hoofdsteden van Europese landen...")

for land, feiten in landen_feiten.items():
    if 'hoofdstad' in feiten:
        hoofdstad = feiten['hoofdstad']
        print(f"{land}: {hoofdstad}")