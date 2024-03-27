import google.generativeai as genai

class Ai:
    def gemini(qna_dict,API_KEY):
        genai.configure(api_key=API_KEY)

        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
        }

        model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                    generation_config=generation_config,
                                    )
        try:
            convo = model.start_chat(
                history=[
                    {
                        "role": "user",
                        "parts": [
                            """
                    You are an expert quiz solver. You are provied with a quiz, which has couple of questions mentioned as "question" and couple of options, with a serial number for each question and each option. Serial number of option is mentioned as "option_number". Your job is to return an array of correct answers using the "options_number" in same order as the questions were given.
                    
                    You are an expert quiz solver. You are provided with a quiz. The quiz is in a format similar to of list ob objects, where in each object has three properties - "question", "question_number" and "options". The "question" property contains the question, "question_number" contains the serial number of the question and "options" contains an array of objects where each object has two properties - "content" and "option_number". The "content" property contains the option and "option_number" contains the serial number of the option. You have to return an array of correct answers using the "option_number" in the same order as the questions were given.
                    
                    For deciding the correct answer, you have to pick the option which is most relevant to the question.
                    Also remember to use only the "option_number" mentioned for an option to mmake an array of correct answers.
                    
                    If you are unsure about any answer just pick whatever you think will be best but make sure to pick ONLY ONE OPTION FOR EACH QUESTION. NO MORE OR NO LESS THAN ONE.

                    Here is a sample input you will get:
                    
                    [
                        {
                            "question": "Consider a scenario in a server environment where system administrators need to perform routine maintenance tasks and automate server configurations. How does the Command Line Interface (CLI) prove advantageous in this real-time application?",
                            "question_number": 0,
                            "options": [
                                {
                                    "content": "By enhancing video streaming capabilities",
                                    "option_number": 0
                                },
                                {
                                    "content": "By simplifying online shopping experiences",
                                    "option_number": 1
                                },
                                {
                                    "content": "By providing a scriptable and efficient means for remote administration and automation of server tasks",
                                    "option_number": 2
                                },
                                {
                                    "content": "By optimizing social media content delivery",
                                    "option_number": 3
                                }
                            ]
                        },
                        {
                            "question": "How does the Command Line Interface (CLI) contribute to the efficiency and automation of tasks in an Operating System?",
                            "question_number": 1,
                            "options": [
                                {
                                    "content": "By providing advanced image editing tools",
                                    "option_number": 0
                                },
                                {
                                    "content": "By simplifying voice recognition functionalities",
                                    "option_number": 1
                                },
                                {
                                    "content": "By offering a text-based environment for scripting and executing commands",
                                    "option_number": 2
                                },
                                {
                                    "content": "By optimizing file storage and retrieval processes",
                                    "option_number": 3
                                }
                            ]
                        },
                        {
                            "question": "In what way does the operating system enhance user interaction with the computer?",
                            "question_number": 2,
                            "options": [
                                {
                                    "content": "Directly allocating resources to users.",
                                    "option_number": 0
                                },
                                {
                                    "content": "Creating hardware interfaces.",
                                    "option_number": 1
                                },
                                {
                                    "content": "Managing security protocols exclusively.",
                                    "option_number": 2
                                },
                                {
                                    "content": "Providing an interface between the user and hardware.",
                                    "option_number": 3
                                }
                            ]
                        },
                        {
                            "question": "What are the two fundamental approaches for users to interact with the operating system?",
                            "question_number": 3,
                            "options": [
                                {
                                    "content": "Programming and scripting",
                                    "option_number": 0
                                },
                                {
                                    "content": "Command-line interface (CLI) and Graphical user interface (GUI)",
                                    "option_number": 1
                                },
                                {
                                    "content": "File manipulation and resource allocation",
                                    "option_number": 2
                                },
                                {
                                    "content": "Error detection and multitasking",
                                    "option_number": 3
                                }
                            ]
                        },
                        {
                            "question": "Why is the Graphical user interface (GUI) considered more user-friendly?",
                            "question_number": 4,
                            "options": [
                                {
                                    "content": "It allows programming and scripting",
                                    "option_number": 0
                                },
                                {
                                    "content": "It is difficult to learn",
                                    "option_number": 1
                                },
                                {
                                    "content": "It uses menus, icons, and graphical elements",
                                    "option_number": 2
                                },
                                {
                                    "content": "It is less powerful",
                                    "option_number": 3
                                }
                            ]
                        }
                    ]


                    Here is the format of output - 
                    [{corect option_number for question 0},{corect option_number for question 1},{corect option_number for question 2},{corect option_number for question 3},{corect option_number for question 4}]

                    In the end for 5 question your reply should look like this - [1,2,3,3,1]

                    Remember there can be more or less questions than five, so make sure to mention correct option for all questions.
                    """
                        ],
                    },
                    {
                        "role": "model",
                        "parts": {
                            "text": "Understood. I will only pick the correct options for each question and return them in the same order as the questions were given. I will return only an array of correct answers and for making the array I will use the 'option_number' mentioned for an option. I will start solving the quiz now."
                        },
                    },
                ]
            )

            convo.send_message(qna_dict)

            return convo.last.text
        except Exception as e:
            return "[-1,-1,-1,-1,-1]"
