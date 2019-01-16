# EXAMPLES:

nums = range(-3, 6)
print(nums)
small_numbers = [num for num in nums if num < 6]
print(small_numbers)

words = ['big', 'red', 'dog', 'ate', 'his', 'food']
three_letters_words = [ word.title() for word in words if len(word) == 3 ]
print(three_letters_words)

# -----

# EXERCISE:

# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

songs = {
  ('Nickelback', 'How You Remind Me'),
  ('Creed', 'Arms Wide Open'),
  ('Bush', 'Glycerine'),
  ('Live', 'Lightning Crashes'),
  ('Nickelback', 'Animals'),
  ('REM', 'Nightswimming')
}

NBfree_songs = {song[1] for song in songs if song[0] != 'Nickelback'}
print(NBfree_songs)


# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

