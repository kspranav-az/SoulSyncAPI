from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # For handling HTTP status codes
import google.generativeai as genai
# from profanity_check import predict
# import pickle
# from keras.models import load_model
# from keras.preprocessing.sequence import pad_sequences


# model = load_model("model.h5")
# tokenizer = pickle.load(open('tokenizer.pickle', 'rb'))

class ChatView(APIView):
    def get(self, request):
        # Get the message from the request data (assuming JSON format)
        message = request.data.get('message')

        # Check if message is provided
        if not message:
            return Response({'error': 'Please provide a message.'}, status=status.HTTP_400_BAD_REQUEST)

        # Configure the Gemini API (replace with your API key)
        genai.configure(api_key="AIzaSyB6a8EE1z4qIPbOU8YFZEspTpMZ-gsXnV4")

        # Create a model object (replace 'gemini-pro' if using a different model)
        model = genai.GenerativeModel('gemini-pro')

        # Generate response using the model
        response = model.generate_content(contents=[{'parts': [{'text': "act as a mental health companion for\
         the following messages\
         (give answers within 25 words)  :"+ message}]}])

        # Get the generated text from the response
        generated_text = response.text

        # Prepare the response data
        response_data = {'message': generated_text}

        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request):
        # Get the message from the request data (assuming JSON format)
        message = request.POST['message']

        if not message:
            return Response({'error': 'Please provide a message.'}, status=status.HTTP_400_BAD_REQUEST)

        # Configure the Gemini API (replace with your API key)
        genai.configure(api_key="AIzaSyB6a8EE1z4qIPbOU8YFZEspTpMZ-gsXnV4")

        # Create a model object (replace 'gemini-pro' if using a different model)
        model = genai.GenerativeModel('gemini-pro')


        # Generate response using the model
        response = model.generate_content(contents=[{'parts': [{'text': message}]}])

        # Get the generated text from the response


        generated_text = response.text

        # Prepare the response data
        response_data = {'message': generated_text}

        return Response(response_data, status=status.HTTP_200_OK)


# class ProfanityView(APIView):
#     def post(self,request):
#         message = request.POST['message']
#
#         if not message:
#             return Response({'error': 'Please provide a message.'}, status=status.HTTP_400_BAD_REQUEST)
#
#         response_data = {'message':predict(message)}
#
#         return Response(response_data, status=status.HTTP_200_OK)

# class SentimentView(APIView):
#     def post(self,request):
#
#         message = request.POST['message']
#
#         if not message:
#             return Response({'error': 'Please provide a message.'}, status=status.HTTP_400_BAD_REQUEST)
#
#
#         # Tokenize the input text
#         tokenized_text = tokenizer.texts_to_sequences([message])
#
#         # Pad sequences
#         padded_text = pad_sequences(tokenized_text, maxlen=250)
#
#         # Make predictions using the loaded model
#         predictions = model.predict(padded_text)
#
#         response_data = {'message': predictions}
#
#         return Response(response_data, status=status.HTTP_200_OK)