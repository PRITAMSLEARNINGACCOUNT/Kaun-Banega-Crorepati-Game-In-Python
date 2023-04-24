Question_lst = []  # Empty List
Answer_List = []  # Empty List
Answer_option_list = []  # Empty List
hello = 2
options = 0
import os
import pyAesCrypt


def cheeck(str, lst):
  temp = options
  for func1 in range(4):
    if str == lst[temp]:
      Answer_List.append(str)
      return 1
    temp = temp + 1


print("This Part Is For Setting Up The Game(Not For Users)")
n = 2
write = open("Question_List.txt", "w")
for i in range(n):
  print("Enter The ", i + 1, " Question")
  ele = str(input())
  Question_lst.append(ele)
  write.write(ele + "\n")
password = input(
  "Enter the Password To Encrypt every questons with their answer??\n")

buffer_size = 64 * 1024

write.close()
with open("Question_List.txt", "rb") as f_in:
  with open("Encrypted_File.txt", "wb") as f_out:
    pyAesCrypt.encryptStream(f_in, f_out, password, buffer_size)
os.remove("Question_List.txt")
option = open("option_list.txt", "w")
for ia in range(n):
  print("\n")
  print(Question_lst[ia])
  print("Enter The Options of the above question(maximum of 4 options)")
  for iaf in range(4):
    lef = str(input(f"Enter option no. {iaf+1}\n"))
    Answer_option_list.append(lef)
    option.write(lef + "\n")
option.close()
with open("option_list.txt", "rb") as f_in:
  with open("Encrypted_Option_List.txt", "wb") as f_out:
    pyAesCrypt.encryptStream(f_in, f_out, password, buffer_size)
os.remove("option_list.txt")
correct_answer = open("correct_answer.txt", "w")
for answer1 in range(n):
  print("\n")
  print(f"the queston is {Question_lst[answer1]}")
  print("now these are the options of the above question\n")
  temp2 = options
  for show in range(4):
    print(Answer_option_list[temp2])
    temp2 = temp2 + 1
  string = input(
    f"Now Enter the Correct answer of the above question from the above options\n"
  )

  while 20 > 4:
    if cheeck(string, Answer_option_list) == 1:
      correct_answer.write(string + "\n")
      break
    else:
      print("your given answer is not matched in available options.")
      string = input(f"Enter the answer of question no. {answer1+1}\n")
      hello = hello + 1
      continue

  options = options + 4
correct_answer.close()
with open("correct_answer.txt", "rb") as f_in:
  with open("Encrypted_Correct_Answer.txt", "wb") as f_out:
    pyAesCrypt.encryptStream(f_in, f_out, password, buffer_size)
os.remove("correct_answer.txt")
