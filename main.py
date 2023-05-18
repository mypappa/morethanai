import re
from flask import Flask, render_template, request, url_for
import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory


# Lang Chain Objects - link to OpenAI
llm = OpenAI(temperature=0.4)
conversation = ConversationChain(
    llm=llm, 
    verbose=False, 
    memory=ConversationBufferMemory()
)

# Flask Objects
app = Flask(  # Create a flask app
  __name__,
  template_folder='templates',  # Name of html file folder
  static_folder='static'  # Name of directory for static files
)

#init promt
initial_promt = "you are an AI creating a story in collaboration with humans. The topic of the story is 'a romantic story between a humanoid and a plant'. The story never ends but is a cumulative process of human input and AI integration of the input. Start writing a short fictional story of maximum 5 lines and finish by asking only one concrete question of maximum 3 lines to the humans (that are not part of the story) about important information for the plot to continue the storyline. This question starts with the words: \"Dear collaborators\".... Make this a loop. then you integrate the answer you get and rewrite the story accordingly."

# initial promt
story = conversation.predict(input=initial_promt)
idx_question = story.find('Dear collaborators')

story_memory = []
did_the_story_end = False

story_memory.append(story[:idx_question])
current_question = story[idx_question:]

print("answer to initial prompt")
print(story)
print("-----------------------------------")
print(story[idx_question:])
print("-----------------------------------")

# the link to wep-page HOME (live)
@app.route('/', methods = ['GET'])
def story_page():
  global story_memory
  return render_template('story.html', web_story=story_memory)


@app.route('/get_story', methods = ['GET'])
def get_story():
  global story_memory
  return {"story": story_memory} 


# the link to wep-page QUESTIONS (live)
@app.route('/questions', methods = ['GET'])  
def questions_page():
  global current_question
  return render_template('questions.html', web_question=current_question)


@app.route('/questions', methods = ['POST'])
def post_answer():
  global story_memory, did_the_story_end
  
  content = request.json
  answer = content['answer']
  answer = re.sub(r"[\n\t\s]*", "", answer)
  print("answer is: ", answer)

  if answer.lower() == "magicword":
    closing_prompt = "end the story in a creative and beautiful way in nomore than 6 lines. Do not end with a question"
    story = conversation.predict(input=closing_prompt)
    did_the_story_end = True
  else:
    loop_prompt = (
        f"continue the existing story based on this answer: {answer}. the continuation of the story will again end with a question that starts with the words: 'Dear collaborators'. Make this continuation not longer than 4 lines. then again ask a new question awaiting the answer to let them direct the storyline and so on"  
    )
    story = conversation.predict(input=loop_prompt)
  
  idx_question = story.find('Dear collaborators')

  new_story = story[:idx_question]
  new_question = story[idx_question:]

  q = open("questionmemory.txt", "at")
  q.write(new_question)
  q.write("\n")
  q.close()

  s = open("storymemory.txt", "at")
  s.write(new_story)
  s.write("\n")
  s.close()

  a = open("answermemory.txt", "at")
  a.write(answer)
  a.write("\n")
  a.close()

  story_memory.append(new_story)
  if did_the_story_end is True:
    return {"question": "The story has ended"}
  return {"question": new_question}


if __name__ == "__main__":  
  
  app.run(host='0.0.0.0',  port=80, debug=True)
