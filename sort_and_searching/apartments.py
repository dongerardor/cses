applicants_apartments_diff_input = input()
desired_sizes_input = input()
apartment_sizes_input = input()

applicants = 0
apartments_qty = 0
diff = 0

applicants, apartments_qty, diff = [int(x) for x in applicants_apartments_diff_input.split()]
desired_sizes = [int(x) for x in desired_sizes_input.split()]

def is_in_range(apartment, desired_size, diff):
    if apartment >= desired_size - diff:
        if apartment <= desired_size + diff:
            return True
    return False

apartments = sorted([int(x) for x in apartment_sizes_input.split()])

apartments_assigned = 0

for desired_size in desired_sizes:
    for i, apartment in enumerate(apartments):
        if is_in_range(apartment, desired_size, diff):
            apartments_assigned += 1

# print(applicants)
# print(apartments)
# print(diff)
# print(desired_sizes)
# print(apartment_sizes)
#while apartment < len(apartments):