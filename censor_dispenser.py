# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
import re
def censor_word(word_to_censor, email):
  censored_email = email.replace(word_to_censor, "beep-boop")
  return censored_email

#print(censor_word("month", email_one))

def censor_list(list_to_censor, email):
  censored_email = email
  for i in range(len(list_to_censor)):
    word_to_reverse = list_to_censor[i]
    reversed_word = word_to_reverse[::-1]
    censored_email = censored_email.replace(list_to_censor[i], reversed_word)
  return censored_email

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#print(censor_list(proprietary_terms, email_two))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def sugar_coating(negative_words, email):
  censored_email = censor_list(proprietary_terms, email)
  sliced_email = re.findall(r'\S+|\n',censored_email)
  #print(sliced_email)
  first_indice = float('inf')
  first_indice_word = ""
  for email_index in range(len(sliced_email)):
    for word_index in range(len(negative_words)):
      if negative_words[word_index] in sliced_email[email_index] and email_index < first_indice:
        first_indice = email_index
        first_indice_word = negative_words[word_index]
  #return range(first_indice+1, len(sliced_email))
  for e_index in range(first_indice + 1, len(sliced_email)):
    for n_word in negative_words:
      if n_word in sliced_email[e_index]:
        sliced_email[e_index] = "sugar-coated"
  rejoined_email = " ".join(sliced_email)
  rejoined_email = rejoined_email.replace("\n ", "\n")
  return rejoined_email

#print(sugar_coating(negative_words, email_three))

def censor_like_crazy(negative_words, proprietary_terms, email):
  sliced_email = re.findall(r'\S+|\n',email)
  #print(sliced_email)
  first_indice = float('inf')
  first_indice_word = ""
  for e_index in range(len(sliced_email)):
    for w_index in range(len(negative_words)):
      if negative_words[w_index] in sliced_email[e_index] and e_index < first_indice:
        first_indice = e_index
        first_indice_word = negative_words[w_index]
        if (sliced_email[e_index-1] not in negative_words) and (sliced_email[e_index-1] not in proprietary_terms) and (sliced_email[e_index-1] != "\n"):
          sliced_email[e_index-1] = "before"
        if (sliced_email[e_index+1] not in negative_words) and (sliced_email[e_index+1] not in proprietary_terms) and (sliced_email[e_index+1] != "\n"):
          sliced_email[e_index+1] = "after"
  #return range(first_indice+1, len(sliced_email))
  for e_index in range(first_indice + 1, len(sliced_email)):
    for n_word in negative_words:
      if n_word in sliced_email[e_index]:
        sliced_email[e_index] = "sugar-coated"
        if (sliced_email[e_index-1] not in negative_words) and (sliced_email[e_index-1] not in proprietary_terms) and (sliced_email[e_index-1] != "\n"):
          sliced_email[e_index-1] = "before"
        if (sliced_email[e_index+1] not in negative_words) and (sliced_email[e_index+1] not in proprietary_terms) and (sliced_email[e_index+1] != "\n"):
          sliced_email[e_index+1] = "after"
  for e_index in range(len(sliced_email)):
    for p_index in range(len(proprietary_terms)):
      word_to_reverse = proprietary_terms[p_index]
      reversed_word = word_to_reverse[::-1]
      if proprietary_terms[p_index] in sliced_email[e_index]:
        if (sliced_email[e_index-1] not in negative_words) and (sliced_email[e_index-1] not in proprietary_terms) and (sliced_email[e_index-1] != "\n"):
          sliced_email[e_index-1] = "before"
        if sliced_email[-1] != sliced_email[e_index]:
          if (sliced_email[e_index+1] not in negative_words) and (sliced_email[e_index+1] not in proprietary_terms) and (sliced_email[e_index+1] != "\n"):
            sliced_email[e_index+1] = "after"
      sliced_email[e_index] = sliced_email[e_index].replace(proprietary_terms[p_index], reversed_word)
  
  rejoined_email = " ".join(sliced_email)
  rejoined_email = rejoined_email.replace("\n ", "\n")
  return rejoined_email

print(censor_like_crazy(negative_words, proprietary_terms, email_four))
#print(email_four)