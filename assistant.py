import aiy.voice.tts
from aiy.board import Board
from aiy.cloudspeech import CloudSpeechClient

import supercook as sc
import retriveRecipes as pc
import food_delivery as fd
import habits as h
import appetit_led as l
        
def readStep(steps,index):
    answer = steps[index]
    
    aiy.voice.tts.say(answer)
    if index == len(steps)-1:
        answer = "Enjoy your meal!"
        aiy.voice.tts.say(answer)
        return "0"
    return "5a"


def getRecipeName(nameRecipe):      
    aiy.voice.tts.say("I'm searching..")
    l.set_breathe_RED()
    steps, time_r, calories = pc.getRecipe(nameRecipe)
    l.set_on_GREEN()
    answer = "The chosen recipe requires " + time_r + "minutes, is it fine for you?"
    aiy.voice.tts.say(answer)
    status = "5a"
    return steps, time_r,status


def main():
    l.set_breathe_GREEN()
    client = CloudSpeechClient()
    status = "0"
    ingredients = None
    recipes = {}
    print("Listening...")
    l.set_on_GREEN()
    index = 0
    with Board() as board:
        while True:
            
            text = client.recognize(language_code = "en-US")
            
            if(text is None):
                aiy.voice.tts.say("I do not understand")
                continue
            
            if status == "0":
                if text is not None and any(x in text for x in ["hungry", "food", "eat", "lunch", "dinner"]):
                    print("You said " + text)
                    answer = "Hi, would you like to cook something or would you prefer to order some food?"
                    aiy.voice.tts.say(answer, lang='en-US', volume=90)
                    status = "1"
                elif any(x in text for x in ["finis","end","ending","showoff"]):
                    aiy.voice.tts.say("Goodbye all, thanks for attention and give us our airpods")
                    l.set_off()
                    exit(0)
            

            elif status == "1" and text is not None and any(x in text for x in ["cook", "cooking","prepare"]):
                print("You said " + text)
                if h.check_habits() is True:
                    answer = "You should eat something healthy, do enjoy salad recipes?"                  
                    aiy.voice.tts.say(answer)
                    status = "2ai"
                else:
                    answer = "Nice, what ingredients do you want to use?"
                    aiy.voice.tts.say(answer)
                    status = "2a"
            
            elif status == "2ai":
                if any(x in text for x in ["yes", "ok","good"]):
                    client.stop_listening()
                    steps,time_r,status = getRecipeName("Green Salads")
                    status = "5a"
                    client.start_listening()
                elif any(x in text for x in ["no", "other"]):
                    answer = "So, what ingredients do you want to use?"
                    aiy.voice.tts.say(answer)
                    status = "2a"                   
            
            elif status == "2a" and text is not None:
               
                client.stop_listening()
                ingredients = text.replace("and", "").replace("some", "").split(" ")
                print(ingredients)
                recipes, needs, urls = sc.getRecipeName(ingredients)
                menu = " ".join(recipes.values())
                answer = "I have found these recipes, " + menu + "Which one do you want to prepare?"
                aiy.voice.tts.say(answer)
                client.start_listening()
                status = "3a"

            elif status == "3a" and text is not None:
                #print("You said " + text)
                if text is not None:
                    
                    if "first" in text or recipes[0] in text:
                        client.stop_listening()
                        steps,time_r,status = getRecipeName(recipes[0])
                        client.start_listening()
                    elif "second" in text or recipes[1] in text:
                        if recipes[1]is not None:
                            steps,time_r,status = getRecipeName(recipes[1])
                            client.start_listening()
                        else:
                            steps,time_r,status = getRecipeName(recipes[0])
                            client.start_listening()
                    elif "third" in text or recipes[2] in text:
                        client.stop_listening()
                        if recipes[2] is not None:
                            steps,time_r,status = getRecipeName(recipes[2])
                            client.start_listening()
                        else:
                            steps,time_r,status = getRecipeName(recipes[0])
                            client.start_listening()

            elif status == "5a" and text is not None:
                if any (x in text for x in ["stop", "finish", "end"]):
                    aiy.voice.tts.say("Sorry, my lord")
                    status = "0"
                elif text is not None and any(x in text for x in ["next", "yes","ok","okay"]):
                    status = readStep(steps,index)
                    index += 1


            #BRANCH CIBO D'ASPORTO
            elif status == "1" and text is not None and any(x in text for x in ["order", "take", "buy"]):
                print("You said " + text)
                food = h.ask_best_food()
                if food != "":
                    status = "4b"
                    answer = "I think you might like "+food+", would you like that again?"
                    #TODO status
                    aiy.voice.tts.say(answer)
                else:
                    answer = "Good, what do you want to eat?"
                    status = "2b"
                    aiy.voice.tts.say(answer)


            elif status == "4b" and text is not None and any(x in text for x in ["yes", "no"]):
                if "yes" in text:
                    status = "3b"
                if "no" in text:
                    h.set_token_wrong_food()
                    status = "2b"
                    answer = "I am sorry, I'll try to do better next time! What would you like, then?"
                    aiy.voice.tts.say(answer)
                   

            elif status == "2b" and text is not None:
                print("You said " + text)
                dish = text.replace("like", "").replace("would", "").replace("want", "").replace("I'd", "").replace("I", "").lower()
                l.set_breathe_RED()
                name, price = fd.order_food(dish)
                h.new_order(dish)
                l.set_on_GREEN()
                if price != -1:
                    answer = "I found " + dish + ", the best price is " + str(price) + " euro at " + name + ". Is it fine for you?"
                    aiy.voice.tts.say(answer)
                    status = "3b"
                else:
                    answer = "I did not find anything"
                    aiy.voice.tts.say(answer)
                    status = "0"

            elif status == "3b" and text is not None:
                print("You said " + text)
                if "yes" in text:
                    #avverti il boss
                    answer = "All done, i'm ordering for you"
                    aiy.voice.tts.say(answer)
                    status = "0"
                if "no" in text:
                    answer = "Okay, i will not order anything"
                    aiy.voice.tts.say(answer)
                    status = "0"
                

if __name__ == "__main__":
    main()
    


    