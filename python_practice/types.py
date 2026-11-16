# Numeric and sequence types
user_id = 42                        # int (immutable)
coordinates = (10.5, 20.3)          # tuple (immutable sequence)
permissions = ["read", "write"]     # list (mutable sequence)

# Mapping type
user_metadata = {"theme": "dark", "notifications": True} # dict (mutable mapping)

# Type conversion (casting)
id_as_string = str(user_id)         # Converts int '42' to str '42'
unique_permissions = set(permissions) # Converts list to a set

# Demonstrating mutability behavior
permissions.append("execute")       # Modifies the original list in place
print(permissions)                  # Output: ['read', 'write', 'execute']