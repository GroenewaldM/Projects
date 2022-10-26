
def greedy_cow_transport(all_cows, allowed_weight):
    weight_used = 0
    previous_weight = 0
    transport_groups = []
    all_cows_copy = all_cows.copy()
    transport = []
    cow_names = []
    cow_weights = []
    while len(cow_weights) < len(all_cows_copy):
        for cow in all_cows:
            if all_cows[cow] > previous_weight:
                previous_weight = all_cows[cow]
                previous_name = cow
        all_cows.pop(previous_name)
        cow_weights.append(previous_weight)
        cow_names.append(previous_name)
        previous_weight = 0    


    while len(cow_names) != 0:
        cow_names_copy = cow_names[:]
        cow_weights_copy = cow_weights[:]
        for i in range(len(cow_names_copy)):
            weight_used += cow_weights_copy[i]
            if weight_used <= allowed_weight:
                transport_groups.append(cow_names_copy[i])
                cow_names.remove(cow_names_copy[i])
                cow_weights.remove(cow_weights_copy[i])
            else:
                weight_used -= cow_weights_copy[i]   
        transport.append(transport_groups)
        transport_groups = []
        weight_used = 0
        
    return transport
all_cows = {'Horns': 50, 'Muscles': 65, 'Milkshake': 75, 'Lotus': 10, 'Louis': 45, 'Miss Bella': 15, 'Polaris': 20, 'MooMoo': 85, 'Patches': 60, 'Clover': 5}
print(greedy_cow_transport(all_cows, 100))  
print(greedy_cow_transport({'Betsy': 39, 'Rose': 42, 'Willow': 59, 'Buttercup': 11, 'Coco': 59, 'Luna': 41, 'Abby': 28, 'Starlight': 54}, 120))    
        
    
    