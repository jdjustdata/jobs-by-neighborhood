# Global Helper function to generate a case-insensitive
# sorting query (use return values with .extra() query)
# Django's queries do not mix upper case and lower case in sort order
# This function will ignore case in sorting 
# (e.g., 'abc', 'Apple', 'art' ... instead of ... 'abc', 'art', 'Apple')

# Sort_Field_Name parameter may have a starting '-' to indicate the sort order is Descending
# Otherwise the sort order is assumed Ascending
def case_insensitive_criteria(sort_field_name):
    if sort_field_name[0] == '-':
        order_field = '-lower_field'
    else:
        order_field = 'lower_field'
    field_name_only = sort_field_name.strip('-')
    lower_field = "lower(" + field_name_only + ")"
    return (lower_field, order_field)

