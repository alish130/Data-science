def companies_by_countries(plant_locations, plant_managers):
    output_dict = {}
    for company, location in plant_locations:
        country = location.split(", ")[-1]
        manager = next((manager for comp, manager in plant_managers if comp == company), None)
        output_dict[country] = [company, location, manager]
    return output_dict
plant_managers = [('Ford', 'Bruce Mills'), ('Tata', 'Rajan Seth'), ('Suzuki', 'Hiroshi Nakamoto'),
                  ('BMW', 'Josh Wagner'), ('Hyundai', ' Narishu Ichiba')]
plant_locations = [('Ford', 'New Hampshire, USA'), ('Tata', 'Guragaun, India'), ('Suzuki', 'Kyoto, Japan'),
                   ('BMW', 'Munich, Germany'), ('Hyundai', 'Seoul, South Korea')]
output_dict = companies_by_countries(plant_locations, plant_managers)
print(output_dict)
