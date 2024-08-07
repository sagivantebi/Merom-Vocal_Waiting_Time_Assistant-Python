answer_dict = {
    'value': 'no internet',
    'children': [
        {
            'value': 'Could you please check if the router is on, and the power LED is blinking?',
            'children': [
                {
                    'value': 'no',
                    'children': [
                        {
                            'value': "Okay, turn on the router with the power button. It's at the bottom of the router. Is the power LED on?",
                            'children': [
                                {
                                    'value': 'no',
                                    'children': [
                                        {
                                            'value': "Oh, that's a problem I can't solve. Please wait for my human colleague to connect."
                                        }
                                    ]
                                },
                                {
                                    'value': 'yes',
                                    'children': [
                                        {
                                            'value': 'Great! Does the internet work now?',
                                            'children': [
                                                {
                                                    'value': 'yes',
                                                    'children': [
                                                        {
                                                            'value': 'Great! If everything is working fine, you can disconnect now. Have a nice day!'
                                                        }
                                                    ]
                                                },
                                                {
                                                    'value': 'no',
                                                    'children': [
                                                        {
                                                            'value': "Oh, that's a problem I can't solve. Please wait for my human colleague to connect."
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    'value': 'yes',
                    'children': [
                        {
                            'value': 'Try to turn off the router, wait five seconds and turn on the router. Is the internet still out?',
                            'children': [
                                {
                                    'value': 'yes',
                                    'children': [
                                        {
                                            'value': 'Great! If everything is working fine, you can disconnect now. Have a nice day!'
                                        }
                                    ]
                                },
                                {
                                    'value': 'no',
                                    'children': [
                                        {
                                            'value': 'I see, which model of router do you have?',
                                            'children': [
                                                {
                                                    'value': 'model A1',
                                                    'children': [
                                                        {
                                                            'value': "Okay, on the front of your model there are two LEDs titled 'LAN' and 'internet'. Please go to the router and say aloud which LEDs are on and which are off.",
                                                            'children': [
                                                                {
                                                                    'value': 'LAN LED is on, internet LED is off',
                                                                    'children': [
                                                                        {
                                                                            'value': "Alright, this problem is a little too complicated for me. Please wait for my human colleague to answer."
                                                                        }
                                                                    ]
                                                                },
                                                                {
                                                                    'value': 'LAN LED is off, internet LED is on',
                                                                    'children': [
                                                                        {
                                                                            'value': "Alright, try to plug the cable in the back of the router into a different socket and check if the internet works now.",
                                                                            'children': [
                                                                                {
                                                                                    'value': 'yes',
                                                                                    'children': [
                                                                                        {
                                                                                            'value': 'Great! If everything is working fine, you can disconnect now. Have a nice day!'
                                                                                        }
                                                                                    ]
                                                                                },
                                                                                {
                                                                                    'value': 'no',
                                                                                    'children': [
                                                                                        {
                                                                                            'value': "Oh, that's a problem I can't solve. Please wait for my human colleague to connect."
                                                                                        }
                                                                                    ]
                                                                                }
                                                                            ]
                                                                        }
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

demo_dict = {
    'value': "Hi! I'm Merom, your virtual assistant. Can I help with your problem while you wait?",
    'children': [
        {
            'value': "Yes, my internet isn't working.",
            'children': [
                {
                    'value': "Could you please check if the router is on, are there any blinking LEDs?",
                    'children': [
                        {
                            'value': "Yes, the PON LED is blinking.",
                            'children': [
                                {
                                    'value': "Okay, I can see that there was a problem in the building. Can you try to unplug the network cable at the back of the router, wait a few seconds, and plug it back in?",
                                    'children': [
                                        {
                                            'value': "yes, one second",
                                            'children': [
                                                {
                                                    'value': "Alright, is the internet working now?",
                                                    'children': [
                                                        {
                                                            'value': "yes, thanks!",
                                                            'children': [
                                                                {
                                                                    'value': "Great! If everything is working fine, you can disconnect now. Have a nice day!"
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

loop_prompt = [
    "hi chat! I have the following protocol for answering a customer calling with a technical problem with their router: ",
    str(demo_dict),
    "\nThe customer said 'Yes, my internet isn't working', I said 'Could you please check if the router is on, are there any blinking LEDs?'",
    "\nThe customer said 'Yes, the PON LED is blinking', What should I tell the customer according to the protocol?",
    "\nPlease answer in the format: 'value' : <reply> \n 'summary' : <summary of the conversation between me and the customer> $$$"
]
