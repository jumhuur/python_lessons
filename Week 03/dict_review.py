user = {
    "name": "maxamad",
    "age": 26,
    "skills" : ["Html", "Css", "Js"]
}

print(user)

# get(keys)
#👉 Hel value-ga fure gaar ah; error ma keeno haddii uusan jirin.
print(user.get("name"))
print(user.get("age"))
print(user.get("skills"))


# keys()
# 👉 Soo celi dhammaan furayaasha (keys).
keys = user.keys()
print(keys)
print(type(keys))  # <class 'dict_keys'>

#values()
# 👉 Soo celi dhammaan qiimaha (values).
print(user.values())
print(type(user.values()))  # <class 'dict_values'>

# items()
# 👉 Soo celi key-value dhamaan — tuple ahaan.
print(user.items())

# update(other_dict)
# 👉 Ku dar dictionary kale ama bedel value-ga key jira.
user.update({'job': "developer"})
print(user["job"])


# pop(key)
#👉 Ka saar key-ga la rabo, una celi value-ga.
removed = user.pop("age")
print(removed)
print(user)


## popitem()
# 👉 Ka saar item random ah (version hore: item ugu dambeeya).
print(user.popitem())
print(user)

# setdefault(key, default)
# 👉 Haddii key-ga jiro → celi value-giisa. Haddii uusan jirin → samee.
print(user.setdefault("country", "soomaliland"))
print(user.setdefault("Active", False))
print(user.setdefault("name", "unknown"))

#clear()
# 👉 Tirtir dhammaan key-value pairs.
user.clear()
print(user)