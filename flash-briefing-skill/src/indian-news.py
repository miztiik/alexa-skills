
#### Ref - https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/understanding-the-flash-briefing-skill-api

# My First Alexa Ask - Flask App

@ask.launch
def start_skill():
    welcome_message = 'Hello Naveen, would you like the news?'
    return question(welcome_message)

@ask.intent('YesIntent')
def share_headlines():
    headlines = get_headlines()
    headline_msg = 'The current world news is {}'.format ( headlines )
    return statement ( headline_msg )

@ask.intent('NoIntent')
def no_intent():
    bye_text = "I am not sure why you asked me to run then, But then have a nice day..."
    return statement( bye_text )





# import time
# start = time.time()
# execfile('newsParser.py')
# end = time.time()
# print(end - start)
