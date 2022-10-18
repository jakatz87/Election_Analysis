voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    key=county_dict['county']
    value=county_dict['registered_voters']
    print(f"{key} county has {value} registered voters.")