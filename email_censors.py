# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:


email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# Email_One --------------------------

def censor_one(email, term = "learning algorithms"):
  new_email = email
  new_email = new_email.replace(term, 
  "[*********]")
  return new_email

# print(censor_one(email_one, "learning algorithms"))

# End Email_One--------------------

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

# Email_two -----------------------
def censor_two(email, lst):
  email_in_lower = email.lower()
  # make it a list since strings are immutable
  email = list(email)
  for term in lst:
    index = 0
    while index < len(email):
      index = email_in_lower.find(term, index)
      # if nothing more is found, -1 is returned
      if index == -1:
        break
      if email[index-1] == ' ' or email[index-1] == '\n':
        for i in range(index, index + len(term)):
          email[i] = '*'
      index += len(term)
  email = ''.join(email)
  return email

#  print(censor_two(email_two, proprietary_terms))

# END OF Email_Two---------------------

# Email_three-----------------------


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_three(email, lst):
  email = censor_two(email_three, proprietary_terms)
  email_in_lower = email.lower()
  email = list(email)
  indexes = []
  for term in lst:
    index = email_in_lower.find(term)
    if index != -1:
      indexes.append(index)
  indexes.sort()
  for term in lst:
    index = indexes[0] + 1
    while index < len(email):
      index = email_in_lower.find(term, index)
      if index == -1:
        break
      if email[index-1] == ' ' or email[index-1] == '\n':
        for i in range(index, index + len(term)):
          email[i] = '*'
      index += len(term)
  email = ''.join(email)
  return email
# print(censor_three(email_three, negative_words))

# END Email_three-------------------------------

# Start Email_for------------------------

censor_words = proprietary_terms + negative_words

def censor_four(email, lst):
  email_split = email.split()
  censor_words_indexes = []
  new_indexes = []
  for i in range(len(email_split)):
    for j in range(len(lst)):
      if email_split[i].lower() == lst[j] or email_split[i][:-1].lower() == lst[j]:
        censor_words_indexes.append(i)
  for i in censor_words_indexes:
    new_indexes.append(i - 1)
    new_indexes.append(i)
    new_indexes.append(i + 1)
  
  for i in new_indexes:
    email_split[i] = len(email_split[i]) * '*'
  
  email_split = ' '.join(email_split)
  return email_split

print(censor_four(email_four, censor_words))
