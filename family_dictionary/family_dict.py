my_family = {
  'sister': {
      'name': 'Teela',
      'age': 37
  },
  'mother': {
      'name': 'The Sorceress',
      'age': 65
  },
  'father': {
    'name': 'He-Man',
    'age': 66,
  },
  'brother': {
    'name': 'Cringer',
    'age': 29
  }
}

my_fam = {f"{v['name']} is my {k} and is {str(v['age'])} years old" for (k,v) in my_family.items()}
print(my_fam)
