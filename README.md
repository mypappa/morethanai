# more thAn I  
an interactive installation where humans and artificial intelligences collaborate in unprecedented ways to co-create a story.  

## concept  
we wonder..  
- What happens if we revert The roles between the users and the servers?  
- How can I become the assistant of an AI? then who is the master of whom?  

this project aims to materialise and embody the ways in which artificial intelligences (AI) affect the creation of stories and how human inputs together with nonhuman processing (AI) give us a more-than-human outcome.   

## hands-on  
we will create an interface that records speech, transcribes it to text and feeds it into a language model (which in this case is GPT). Then the AI starts generating a story. The story always ends with a question to the participants for new human input. The answer is then integrated to the story from the AI, live-projected and ends with another question. this continues until we reach an x amount of words

## What we did (and did not do(ourselves)) in technical terms. 
knowing relatively nothing about coding and how to build *digital interfaces* was an interesting starting point for our project “more thAn I” that includes a complex structure of code and *(strange)* languages. With a lot of help we made our scaffold and now can work on a understandable set up without relying on the many knowledgeable minds that guided us till this point. **Great thanks** to **Pietro, Mikel, Xavier, Victor,** and **Aurel** *(@FabLab, we know you know BUT woman power is definitely needed here!)*

### technicalities
we want to enable a human and an AI (our vision a visual and text generating AI) to collaborate on writing a fictional story. We use a *“LangChain”* framework for developing applications that deal with language models, we use a *“GPT”* language model by *“OpenAI”* with the *“davinci”* configuration, we use the open-source web framework *“Flask”* that is written in *“python”* to make our application a responsive webpage and we use *“SpeechRecognition”* which is a pre-built interface of *“javascript”* to transform audio (speech) to text. In our coding environment we use *python*, *javascript*, *HTML* and *CSS*. We work with open-source software and have our codes in a repo for everyone to access. 

#### what we came across and we learned to understand in our own words: 
**Interface:** term used in programming; describes a set of rules that define how different software components (will) interact with each other. It is the “cover” / the interface allows the user to interact with software, without exposing the internal workings of the underlying code.

**API:** Application Programming Interface, so this speaks specifically about how applicatioins communicate with each other. API are offered by platform like facebook, services like paypal, or providers like googlemaps to allow cross-linkages and integration in bigger (software) systems. 

**Visual generating AI:** uses algorithms and models trained on large datasets to create new visual content based on the patterns and information it has learned.

**text generating AI:** uses natural language processing techniques, deep learning models, and language models (@LLMs) trained on large datasets to generate coherent (and relevant) written content-

**LLMs:** large language models that are made to understand and generate human-like text. They are trained on large datasets to learn human languages. 

**python:** programming language often used in web development and data analysis. It comes with a big set of pre-built modules and functions for a lot of tasks and has an easy system to import external libraries and frameworks for specific domains. 

**HTML:** Hypertext Markup Language, a standard markup language used to create web pages [markup: practice of adding special annotations and tags to text to provide structure and formatting instructions]. It often creates a set of instructions that tells web browsers how to display content.

**markdown:** another language to apply markup to text. Simpler and more intuitive way to format text. 

**CSS:** Cascading Style Sheet, a style sheet language the describes the presentation and visual formatting of HTML and other text-structured documents. 

**javascript:** a programming language that runs directly in a web browser (one of the few). It allows to add interactive and dynamic elements and behaviour to websites, e.g. it enables websites to respond to user actions, manipulate content, and interact with external resources. Similarly to python, it comes with a big set of pre-built modules and functions for a lot of tasks and has an easy system to import external libraries and frameworks for specific domains. 
 
Running code in a **local (on my computer) environment** vs. in an **online environment:** local allows full control over development setup and I have offline access but need to install all libraries and necessary languages on my disk. Online is convenient when working together and I can store the necessary additional datasets online.

**GPT:** Generative Pre-trained Transformer. A type of language model developed by OpenAI that has exists in different versions (GPT-2, GPT-3, GPT-4 ect.). 

**Davinci:** a name that OpenAI has given to SPECIFIC configurations of their language models (a very capable and large variation) e.g. GPT-3 and GPT-4 are having these configurations.

<br> 

#### We installed: 

**OpenAI** (python library): needed to access the OpenAI APIs (interfaces). When having an account to use ChatGPT for example, I can ask for my API key which I need to integrate OpenAI services into my system. In OpenAI I have “tokens” (because it is not open-source anymore) that I need to use the API. If my tokes are used up I can only buy new ones. 

**Flask** (library): open-source web framework that is written in python. It is like a foundation / structure that helps to make a python code a web application. You can create routes that define how applications are responding to different URLs. It is a way to make a website out of your code. 

**LangChain** (library): is a python library that provides open-source frameworks to develop applications that deal with (large) language models. Its idea is to “chain” together different components to create more advanced use cases around LLMs like chatbots and generative question-answering. 

**SpeechRecognition** (library): is a javascript library that serves as a Web Speech API (interface). It enable to record, detect, and transcribe audio (speech) into written text. 

### proof of concept
once we had formed the idea and were able to analyse the process we had to follow, we started testing if and how this communication with the AIs could work. Using the ChatGPT we wrote various prompts until we managed to get the output we envisioned. 

However, the ChatGPT is an application of the GPT language model so it already has many more functions built-in like the memory and the chat interface. This meant that we tested the prompts in an 'ideal' environment which we then had to rebuild manually..

our first prompt: 
*You are an AI creating a story on the topic of "more than human communication" . The story never ends.  Start writing a fictional scenario, but only a short beginning of it,  that revolves around the topic of 'more than human' communication. Once you have it, ask a question to the audience (that are not part of the story) about the plot that is necessary for the story to continue. the answer you will get should be intergrated in the script and then will trigger the next question from you to keep going*  

## the code

### importing libraries 
we used 
- 'flask' library to make the python code a web application and create routes to the URLs
- 'langchain' library through which made the connection the OpenAI and created the storage for our conversations

```
import re
from flask import Flask, render_template, request, url_for
import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
```
### creating the files links
```
# Lang Chain Objects - link to OpenAI
llm = OpenAI(temperature=0.5) # adjusting the creativity level
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
```

### initial prompt
When we were experimenting with the ChatGPT we only had to write one single prompt where we could include all the process. But when we built this manually, we had to 'break' the prompt it into three different pieces: the initial prompt, which runs only once in the beginning, the 'loop prompt' which is the one looping, until we reach a good amount of text when we have the 'closing prompt' that ends the story.

```
initial_promt = "you are an AI creating a story in collaboration with humans. The topic of the story is 'a romantic story between a humanoid and a plant'. The story never ends but is a cumulative process of human input and AI integration of the input. Start writing a short fictional story of maximum 5 lines and finish by asking only one concrete question of maximum 3 lines to the humans (that are not part of the story) about important information for the plot to continue the storyline. This question starts with the words: \"Dear collaborators\".... Make this a loop. then you integrate the answer you get and rewrite the story accordingly."
```
### writing the story

```
# setting variables
story = conversation.predict(input=initial_promt) 
idx_question = story.find('Dear collaborators')

# merging stories
story_memory = []
did_the_story_end = False

story_memory.append(story[:idx_question])
current_question = story[idx_question:]

print("answer to initial prompt")
print(story)
print("-----------------------------------")
print(story[idx_question:])
print("-----------------------------------")
```
### link to home webpage
```
@app.route('/', methods = ['GET'])
def story_page():
  global story_memory
  return render_template('story.html', web_story=story_memory)


@app.route('/get_story', methods = ['GET'])
def get_story():
  global story_memory
  return {"story": story_memory} 
```
### link to question webpage
```
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
```
### loop / closing prompt
```
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
```

### text files
```
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
```

### story end
```
  story_memory.append(new_story)
  if did_the_story_end is True:
    return {"question": "The story has ended"}
  return {"question": new_question}


if __name__ == "__main__":  
  
  app.run(host='0.0.0.0',  port=80, debug=True)
```

## References:

• [replit](https://replit.com/~ ); allows programming code in collaboration in an online environment

• [LangChain](https://python.langchain.com/en/latest/index.html) by python; a open-source framework to develop applications that deal with language models

• [SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) by javascript; a open-source Web Speech API

• [Flask](https://flask.palletsprojects.com/en/2.3.x/) by python; a open-source web framework we use to stream and show the (inter)actions

• the best [to look everything up related to the digital interface languages](https://www.w3schools.com/html/default.asp)

• [OpenAI](https://platform.openai.com/docs/models/overview) overview of their models






