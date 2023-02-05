import re

text = "Hi profilehunt1, Someone tried to log in to your Instagram account. If this was you, please use the following code to confirm your identity: 734749 If this wasn't you, please reset your password to"

# Utiliser une expression régulière pour extraire le nombre
match = re.search(r'(\d+)', text)

if match:
  start = match.start()
  end = match.end()
  number = text[start:end]
  print(number) # affiche "734749"
else:
  print("Aucun nombre trouvé dans le texte.")