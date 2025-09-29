from google import genai

''' 
    After create an API key on Google AI Studio and setted on the project
    The API KEY will be automatically recognized if were saved as environment variable GEMINI_API_KEY 
    
    To achieve this go to the terminal, prompt or cmd:
    Windows -> set GEMINI_API_KEY=api-key
    Linux -> export GEMINI_API_KEY=api-key

    verify it was successfully setted with:
    echo $GEMINI_API_KEY 
'''

def get_car_ai_bio(model, brand, year):
    prompt = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres.
    Fale coisas técnicas especificas de esse modelo de carro.
    '''
    
    client = genai.Client()
    
    prompt = prompt.format(brand, model, year)
    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = prompt,
    )
    return response.text