# more thAn I  
an interactive installation where humans and artificial intelligences collaborate in unprecedented ways to co-create a story.  

<img src="https://github.com/mypappa/morethanai/assets/115214510/54f7453d-3b95-4400-b2c7-ac3b2d376cc3"  width="600" height="300">
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

**our first prompt**   
*You are an AI creating a story on the topic of "more than human communication" . The story never ends.  Start writing a fictional scenario, but only a short beginning of it,  that revolves around the topic of 'more than human' communication. Once you have it, ask a question to the audience (that are not part of the story) about the plot that is necessary for the story to continue. the answer you will get should be intergrated in the script and then will trigger the next question from you to keep going*  

## the code

### importing libraries 
we use 
- a 'flask' library to make the python code a web application and create routes to the URLs
- a 'langchain' library through which enables the connection and exchange with OpenAI (and creates the storage for our conversations?)
- a 'OpenAI' library that has its API integrated but which is to be activated with a personalised key (your OpenAI API key)

```
import re
from flask import Flask, render_template, request, url_for
import os
os.environ["OPENAI_API_KEY"] = "YourPersonalOpenAIKey"

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
```

### creating the folders, files and the linkages between the files
- we define our language model and set its creativity level (programmed in temperature) we want it to have(e.g. standard in ChatGPT is temperature=0.7)
- we create folders in which we create HTML files to design and style the webpages

<img width="208" alt="setup" src="https://github.com/mypappa/morethanai/assets/115219314/59559c72-e8f0-4812-b3bc-92238ffcf396">


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
When we were experimenting with the ChatGPT we only had to write one single prompt where we could include all the process. But when building this manually, we have to 'break' the prompt into three different pieces: 
- the initial prompt, which runs only once in the beginning, 
- the 'loop prompt' which is the one that is being repeated until we reach a good amount of text, 
- and a 'closing prompt' that ends the story.

*note that these promts are integrated in the final code in different positions*

```
initial_promt = "you are an AI creating a story in collaboration with humans. The topic of the story is 'a romantic story between a humanoid and a plant'. The story never ends but is a cumulative process of human input and AI integration of the input. Start writing a short fictional story of maximum 5 lines and finish by asking only one concrete question of maximum 3 lines to the humans (that are not part of the story) about important information for the plot to continue the storyline. This question starts with the words: \"Dear collaborators\".... Make this a loop. then you integrate the answer you get and rewrite the story accordingly."

loop_prompt = (
        f"continue the existing story based on this answer: {answer}. the continuation of the story will again end with a question that starts with the words: 'Dear collaborators'. Make this continuation not longer than 4 lines. then again ask a new question awaiting the answer to let them direct the storyline and so on"  
    )
    
closing_prompt = "end the story in a creative and beautiful way in nomore than 6 lines. Do not end with a question"
```
### setting up the seperation between the story and the questions
in this part we set the variables that will define the outputs. We also define that within the written text, the words 'Dear collaborators' are important keywords that will indicate points for splitting the text and direct different parts to different routes. <br> We use the the function **append** to make sure that every new input is **added** to the old one and because we built a **memory function**, it will consider the context from before. <br> <br> The **print** part is a part that only we ill see in the console of our terminal. It is not necessary for the working of the system but helps us to understand wherre we are and recognize fast if things are broken. It will print the story, detect the question that starts with 'dear collabrators' and will put this into a seperate section. 

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
### link it to the story webpage
Here we define the specified route that links HTML to the flask-website. <br> we create two websites that are linked to two different HTML files. One for the story and one for the questions.
 
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
### link it to the question webpage
The question code asks for a little bit more attention because we want that there is always only one question and this has to be the most actual one. So we always need to replace the question after it has been answered with the new accuring questions. <br> <br> Here we also define what happens that if the function *did_the_story_end* is being active, the answer is cleared of all blank spaces and capital letters. It sets all letter to lowercase. This allows the system to recognize later the word which initiailzes the ending promt - *see next paragraph*. 
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
we create a loop that runs constantly until we actively stop it. <br> <br> only if the system detects the answer "magicword" we activate a 'closing prompt' and break the loop and with that end the code. To restart, we have to run the code again from the beginning.  

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

### story end
This is how the answer to the closing promt is being added to the story in the story webpage and how there appears the sentence *The story has ended* instead of a new question in the question webpage. <br> <br> The last line is just a definition of running a weppage online (with flask). It checks if the current module is the *main module* that is being executed. The *port=80* is s standart port for HTTP traffic and specifies whee the application should listen for incoming requests.
```
  story_memory.append(new_story)
  if did_the_story_end is True:
    return {"question": "The story has ended"}
  return {"question": new_question}


if __name__ == "__main__":  
  
  app.run(host='0.0.0.0',  port=80, debug=True)
```


### text files
in order to store separately all the text generated, we made three files: 
- the questions (by the AI), 
- the answers (by the humans) 
- and the story (by the collaboration of AIs and humans).
they are stored in simple text files in no specific folder

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

## References:

• [replit](https://replit.com/~ ); allows programming code in collaboration in an online environment

• [LangChain](https://python.langchain.com/en/latest/index.html) by python; a open-source framework to develop applications that deal with language models

• [SpeechRecognition](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition) by javascript; a open-source Web Speech API

• [Flask](https://flask.palletsprojects.com/en/2.3.x/) by python; a open-source web framework we use to stream and show the (inter)actions

• the best [to look everything up related to the digital interface languages](https://www.w3schools.com/html/default.asp)

• [OpenAI](https://platform.openai.com/docs/models/overview) overview of their models






