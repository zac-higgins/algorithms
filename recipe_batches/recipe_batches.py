#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # set a variable to hold the current highest amount
  batches = []
  for item, amount in recipe.items():
    if ingredients.get(item) is None:
      return 0
    else:
      possible_batches = ingredients.get(item) // amount
      batches.append(possible_batches)
  batches.sort()
  return batches[0]

if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))