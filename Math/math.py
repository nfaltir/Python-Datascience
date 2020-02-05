
r = float(input("\nEnter a radius:"))
def vol(r):
  """ returns volume of  a sphere with radius r """
  v = (4.0/3.0)* 3.14 * r**3
  return v

volume = vol(r)

print("\nThe volume of the sphere is:", round(volume,2),"\n")


