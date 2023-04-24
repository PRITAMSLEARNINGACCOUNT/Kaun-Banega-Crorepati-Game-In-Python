show_option = 0
temp_mpney = 0
money1 = 0
money = [
  1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
  1250000, 2500000, 5000000, 7500000, 10000000, 75000000
]
count = 0
password = "PS0896721234"
import os
import pyAesCrypt

print("The Kaun Banega Corerpati Is Starting Now For Users\n")
print(
  "The Final Amount Of This Game Will Be 7.5 crore Rupees and there are 17 different questions will be asked."
)
buffer_size = 64 * 1024
input_length = os.path.getsize("Encrypted_File.txt")
with open("Encrypted_File.txt", "rb") as f_in:
  with open("Question_file.txt", "wb") as f_out:
    pyAesCrypt.decryptStream(f_in, f_out, password, buffer_size, input_length)
os.remove("Encrypted_File.txt")
n = 2
Question_lst = []  # Empty List
Answer_List = []  # Empty List
Answer_option_list = []  # Empty List
with open("Question_file.txt", "r") as qst_list:
  for i in range(n):
    string = qst_list.readline()
    Question_lst.append(string[:(len(string) - 1)])
buffer_size = 64 * 1024
input_length = os.path.getsize("Encrypted_Option_List.txt")
with open("Encrypted_Option_List.txt", "rb") as f_in:
  with open("Option_List.txt", "wb") as f_out:
    pyAesCrypt.decryptStream(f_in, f_out, password, buffer_size, input_length)
os.remove("Encrypted_Option_List.txt")
with open("Option_List.txt", "r") as hello_world:
  for i in range(n * 4):
    string2 = hello_world.readline()
    Answer_option_list.append(string2[:(len(string2) - 1)])
input_length = os.path.getsize("Encrypted_Correct_Answer.txt")
with open("Encrypted_Correct_Answer.txt", "rb") as f_in:
  with open("Correct_Answer_List.txt", "wb") as f_out:
    pyAesCrypt.decryptStream(f_in, f_out, password, buffer_size, input_length)
os.remove("Encrypted_Correct_Answer.txt")

with open("Correct_Answer_List.txt", "r") as correct_answer:
  for i in range(n):
    string3 = correct_answer.readline()
    Answer_List.append(string3[:(len(string3) - 1)])
for user_questoin in range(n):
  print("\n")
  print(f"So the question no. {user_questoin+1} is \n")
  print(Question_lst[user_questoin])
  print("So the options are .......")
  print(
    f"{Answer_option_list[show_option]} , {Answer_option_list[show_option+1]} , {Answer_option_list[show_option+2]} , {Answer_option_list[show_option+3]}"
  )
  answer_store = input("Enter The answer from above options??\n")
  if answer_store == Answer_List[user_questoin]:
    print(
      f"you have given the correct answer,that's why you won Rs.{money[user_questoin]}"
    )
    temp = money[user_questoin]
    money1 += temp
  else:
    print(
      "you have given the wrong answer or choosen the wrong option,that's why no money on this question"
    )
    break
  show_option = show_option + 4
if money1 > 10000 and money1 < 320000:
  money1 = 10000
elif money1 > 320000 and money1 < 7500000:
  money1 = 320000
elif money1 > 7500000 and money1 < 75000000:
  money1 = 7500000
print(f"so the total amount of money you are taking to your home is {money1}")
