# import time
from pprint import pprint
import openai
# import whisper_api
# import vlc

API_KEY = "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"

openai.api_key = API_KEY

answer_dict = {
    'value': 'no internet',
    'children' : [
        {
            'value' : 'Could you please check if the router is on, and the power led is blinking?',
            'children': [
                {
                    'value': 'no',
                    'children': [
                        {
                            'value': 'Okay, turn on the router with the power button. It\'s at the bottom of the router. Is the power led on?',
                            'children': [
                                {
                                    'value': 'no',
                                    'children': [ {
                                        'value': 'Oh, that\'s a problem I can\'t solve. Please wait for my human colleague to connect'
                                    }]
                                } ,
                                {
                                    'value' : 'yes',
                                    'children': [{
                                        'value': 'Great! does the internet work now?',
                                        'children': [{
                                            'value': 'yes',
                                            'children': [{
                                                'value': 'Great! if everything is working fine, you can disconnect now. Have a nice day!'
                                            } ]
                                        },
                                        {
                                            'value': 'no',
                                            'children': [ {
                                                    'value': 'Oh, that\'s a problem I can\'t solve. Please wait for my human colleague to connect'
                                                }]
                                        }]
                                    }]
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': 'yes',
                    'children': [{
                        'value': 'Try to turn off the router, wait five seconds and turn on the router. Is the internet still out?',
                        'children': [{
                            'value': 'yes',
                            'children': [{
                                'value': 'Great! if everything is working fine, you can disconnect now. Have a nice day!'
                            }]
                        },
                        {
                            'value': 'no',
                            'children': [{
                                'value': 'I see, which model of router do you have?',
                                'children': [{
                                    'value': 'model A1',
                                    'children': [{
                                        'value': 'Okay, in the front of your model there are two LEDs titled \'LAN\' and \'internet\'. please go to the router, and say aloud which LEDs are on and which are off',
                                        'children': [{
                                            'value': 'LAN led is on, internet led is off',
                                            'children': [{
                                                'value': 'Alright, this problem is a little too complicated for me. Please wait for my human colleague to answer'
                                            }]
                                        },
                                        {
                                            'value': 'LAN led is off, internet led is on',
                                            'children': [{
                                                'value': 'Alright, try to plug the cable in the back of the router to a different socket and '
                                                         'check if the internet works now',
                                                'children': [{
                                                    'value': 'yes',
                                                    'children': [{
                                                        'value': 'Great! if everything is working fine, you can disconnect now. Have a nice day!'
                                                    }]
                                                },
                                                {
                                                    'value': 'no',
                                                    'children': [{
                                                        'value': 'Oh, that\'s a problem I can\'t solve. Please wait for my human colleague to connect'
                                                    }]
                                                }
                                                ]
                                            }]
                                        }
                                        ]
                                    }]
                                }]
                            }]
                        }
                        ]
                    }]
                }
            ]
        }
    ]
}


demo_dict = {
    'value': 'Hi! I\'m Merom, your virtual assistant, can I help with your problem while you wait?',
    'children' : [ {
    'value': 'Yes, my internet isn\'t working',
    'children' : [ {
        'value' : 'Could you please check if the'
                  ' router is on, are there any blinking LEDs?',
        'children': [   {
            'value': 'Yes, the PON LED is blinking',
            'children': [ {
                'value': 'Okay, I can see that there was a problem in the building, can you try to unplug the network'
                         ' cable at the back of the router, then wait a few seconds and plug it back?',
                'children': [ {
                    'value': 'yes, one second',
                    'children': [ {
                        'value': 'Alright, is the internet working now?',
                        'children': [ {
                            'value': 'yes, thanks!',
                            'children': [ {
                                'value': 'Great! if everything is working fine, you can disconnect now. Have a nice day!'
                            } ]
                        } ]
                    }]
                    } ]
                } ]
            }]
        } ]
    }]
}

# prompt = ["hi chat! i have the following protocol for answering a customer calling with a technical problem with their router: " ,
#           str(answer_dict),
#           '\nThe customer said "I don\'t have internet", I said  "Could you please check if the router is on, and the power led is blinking?" '
#           '\nThe customer said "no the power led isn\'t on", I said "Okay, turn on the router with the power button. It\'s at the bottom of the router. Is the power led on?" '
#           '\nThe customer said "no the router is connected but the led is off". What Should I say to the customer according to the protocol?',
#           "\nPlease answer in the format: 'value' : <reply> \n 'summary' : <summary of the conversation between me and the customer> $$$"]

loop_prompt = ["hi chat! i have the following protocol for answering a customer calling with a technical problem with their router: " ,
          str(demo_dict),
           "\nThe customer said 'Yes, my internet isn\'t working', I said 'Could you please check if the router is on, are there any blinking LEDs?'",
           "\nThe customer said 'Yes, the PON LED is blinking', What should I tell the customer according to the protocol?",
          "\nPlease answer in the format: 'value' : <reply> \n 'summary' : <summary of the conversation between me and the customer> $$$"]


if __name__ == '__main__':
    api_prompt = ".".join(loop_prompt)
    # instance = vlc.Instance('--no-xlib')
    # mdeia = instance.media_new('Audio/Merom.mp3')
    # duration = mdeia.get_duration()
    # duration_seconds = duration / 1000
    # player = vlc.MediaPlayer("Audio/Merom.mp3")
    # player.play()
    # time.sleep(duration_seconds + 0.01)
    # player.stop()
    # while(True):
    # make api call to openai
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=api_prompt,
        temperature=0,
        max_tokens=1200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["$$$"]
    )
    # # print the parameters and the response
    pprint(response)
    #

