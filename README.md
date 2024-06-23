# fitness-bot

*This is a submission for [Twilio Challenge v24.06.12](https://dev.to/challenges/twilio)*

I used to be hesitant about fitness, worrying about how much effort it would take and what might happen if I did an exercise wrong. I thought it would be too much work, but then I just went for it. Guess what? It's awesome! Fitness is the best way to prolong your life, live to your maximum potential, and keep yourself free from illness. And we've created just the thing you need to get started!

## What We Built
We(@khemraj_bawaskar_f283a984 and I) have developed a fitness bot on Whatsapp designed to support and enhance your fitness journey. Our fitness bot offers motivational fitness quotes, assists in planning your workouts and diet, and schedules reminders to ensure you stay hydrated and eat your meals on time. You can also ask the bot any fitness-related queries, and it will provide the best possible answers and advice.

## Demo
[![FitnessBot Demo](https://img.youtube.com/vi/BWltYXFmZmo/0.jpg)](https://www.youtube.com/watch?v=BWltYXFmZmo)


## Twilio and AI
We have leveraged the WhatsApp Sandbox feature of Twilio to create a bot that utilizes a webhook link for a Flask server. By integrating Azure OpenAI LLM for advanced AI capabilities and Twilio's voice call feature, our bot can call users to remind them about their scheduled reminders.

We have certain commands such as '/tip' or '/dietplan' or '/workoutplan' or '/reminder' or '/query' to generate the response from the bot.

To get into the sandbox, follow this:
![Whatsapp Sandbox](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ixfs1fkutjlpyz0ujo69.png)


When the sandbox starts, the user can get started with '/start' command, which throws the following message: 

*Hi, start your wellness journey now. please use '/tip' or '/dietplan' or '/workoutplan' or '/reminder' or '/query' tag along with the information needed.*
                    
*These templates can be used:*
                    
*'/dietplan weight: 50Kg, height: 5 feet, purpose: muscle-enhancement, non-veg food'*
                    
*'/workoutplan weight: 50Kg, height: 5 feet, purpose: leg-muscles-enhancement, exercise mode: mid'*
                    
*'/query I am unable to feel my back-muscle while doing lat-pull downs. What should I do to improve?'*
                    
*'/reminder Please set an call reminder for lunch at 2 PM on 25/06/2024'*
                    
*'/tip'*

The user can accordingly use the commands and get responses.
1. **/tip:** Provides motivational fitness/workout quotes to keep you inspired.
2. **/reminder:** Helps to schedule a reminder with a time and description, and a voice call comes at the scheduled time to remind the user.
3. **/query:** The bot answers the query with the best possible suggestions.
4. **/workoutplan:** The bot creates a workout plan for the user for a day according to the given weight, height, purpose of the workout, and intensity of the exercise mode.
5. **/dietplan:** The bot creates a diet plan for the user for a day according to the given weight, height, purpose of the diet(for bulking/cutting/normal muscle growth), and preference of the food(veg/non-veg).

