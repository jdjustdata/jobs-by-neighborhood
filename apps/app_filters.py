

# Global Helper function to generate a case-insensitive
# sorting query (use return values with .extra() query)
def case_insensitive_criteria(sort_field_name):
    if sort_field_name[0] == '-':
        order_field = '-lower_field'
    else:
        order_field = 'lower_field'
    field_only = sort_field_name.strip('-')
    lower_field = "lower(" + field_only + ")"
    return (lower_field, order_field)

