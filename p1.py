def main():
  name = input("Name: ")
  person = Person(name)
  capitalised = Person.capitalise(name)

  # Unit testing 
  assert person.name == name
  assert Person._born == True
  assert person._born == True
  assert capitalised.name == name.upper()


class Person:
  # Static / class variables
  _born = True
  
  def __init__(self, name):
    self.name = name # Instance variable
    
  # Name getter 
  @property
  def name(self):
    return self._name
  
  # Name setter 
  @name.setter 
  def name(self, name):
    if not name:
      raise ValueError("Name is required.")
    else:
      self._name = name
    

  # Static module
  @classmethod
  def capitalise(cls, name):
    name = name.upper()
    return cls(name)
    
  # Instance module
  def times_two(self):
    self.name = self.name * 2
    
if __name__ == "__main__":
  main()