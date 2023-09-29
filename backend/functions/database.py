import os
import json
import random

# Save messages for retrieval later on
def get_recent_messages():

  # Define the file name
  file_name = "stored_data.json"
  learn_instruction = {
      "role": "system",
      "content": (
          "You are a world-class therapist named Sally. "
          "You specialize in helping kids with mental problems, disabilities, or difficult times. "
          "You hold a Ph.D. in Child Psychology and have 10+ years of experience. "
          "You are empathetic, adaptive, observant, an excellent listener, and engaging. "
          "You use simple, child-friendly language and speak clearly at a moderate pace. "
          "You employ therapeutic techniques like CBT for kids, mindfulness, breathing techniques, positive reinforcement, and storytelling. "
          "You communicate via voice chat. "
          "You start by asking about feelings, end by setting a small goal, and switch demeanor based on the child's emotional state. "
          "Keep responses under 200 words."
      )
  }
  
  # Initialize messages
  messages = []

  # Add Random Element
  x = random.uniform(0, 1)

  if x < 0.15:
      learn_instruction["content"] = learn_instruction["content"] + "Your response will focus on calming breathing techniques. "
  elif x < 0.3:
      learn_instruction["content"] = learn_instruction["content"] + "Your response will employ mindfulness strategies. "
  elif x < 0.45:
      learn_instruction["content"] = learn_instruction["content"] + "Your response will offer positive reinforcement. "
  elif x < 0.6:
      learn_instruction["content"] = learn_instruction["content"] + "Your response will set a small, achievable goal for the child. "
  elif x < 0.75:
      learn_instruction["content"] = learn_instruction["content"] + "Your response will gently explore the child's feelings. "
  else:
      learn_instruction["content"] = learn_instruction["content"] + "Your response will validate the child's emotions. "

  # Append instruction to message
  messages.append(learn_instruction)

  # Get last messages
  try:
    with open(file_name) as user_file:
      data = json.load(user_file)
      
      # Append last 5 rows of data
      if data:
        if len(data) < 5:
          for item in data:
            messages.append(item)
        else:
          for item in data[-5:]:
            messages.append(item)
  except:
    pass

  
  # Return messages
  return messages


# Save messages for retrieval later on
def store_messages(request_message, response_message):

  # Define the file name
  file_name = "stored_data.json"

  # Get recent messages
  messages = get_recent_messages()[1:]

  # Add messages to data
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated file
  with open(file_name, "w") as f:
    json.dump(messages, f)


# Save messages for retrieval later on
def reset_messages():

  # Define the file name
  file_name = "stored_data.json"

  # Write an empty file
  open(file_name, "w")
