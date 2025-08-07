thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy()
print(x)

x = car.get("model")
print(x)

car.pop("model")
print(car)


car.update({"color": "White"})
print(car)

car.clear()
print(car)
