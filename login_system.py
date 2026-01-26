users={
    "abc123" : "theer@123",
    "theer2310" : "iam143",
    "vish@12" : "mine@2112",
    "sanjay.gowdaa" : "abcd@00"
}
def login(users):
 for count in range(0,3):
  u_id=input("Enter the user id: ")
  password=input("Enter the password: ")
  if u_id in users:
    if users[u_id]==password:
        print("Logged in successfully")
        break
    else:
        print("Incorrect Password")
  else:
    print("Incorrect user id")
  if count<2:
       print("Try again!!")
  else:
       print("3 attempts completed try again later")

