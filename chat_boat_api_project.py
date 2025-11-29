import google.generativeai as genai 
key = "AIzaSyArs4e9WPPtbluG8K-HZND3SMVWh0_gjFA"  #Enter your Gemini API Key , api nahi hai isliye erro aa rha hai ,
print("your key is :",key)
genai.configure(api_key = key)
model = genai.GenerativeModel("gemini-2.5-flash")
# image_model = genai.GenerativeModel("gemini-2.0-flash-image")

while True:
  user = input("Chat with me :")
  if user.lower() == 'exit':  # exit se program terminate ho jayega
    
    print("by by")
    break
  response = model.generate_content(user)
  print("BOT :",response.text)
  

  

