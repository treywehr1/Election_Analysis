voting_data = [
                {'county':'Arapahoe', 'registered_voters': 422829},
                {'county':'Denver', 'registered_voters': 463353}, 
                {'county':'Jefferson', 'registered_voters': 432438}
            ]
# print(voting_data[1]['county'])
maxIndex = -1
maxValue = 0
for county_name in range(len(voting_data)):
    # print(f"{voting_data[county_name]['county']} county has {voting_data[county_name]['registered_voters']} registered voters.")
    if voting_data[county_name]['registered_voters'] > maxValue:
        maxValue = voting_data[county_name]['registered_voters']
        maxIndex = county_name

print(f"{voting_data[maxIndex]['county']} county has {voting_data[maxIndex]['registered_voters']} registered voters.")

# for county_data in voting_data:
#     print(f"{county_data['county']} county has {county_data['registered_voters']} registered voters.")
    

   
        # print(f"{} county has {b} registered voters")

# info_dict = {'name':'Trey', 'pets':'Oakley', 'age': 25}

# print(info_dict['name'])