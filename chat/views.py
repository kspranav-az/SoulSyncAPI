from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # For handling HTTP status codes
import google.generativeai as genai
from profanity_check import predict


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
        response = model.generate_content(contents=[{'parts': [{'text': message}]}])

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


class ProfanityView(APIView):
    def post(self,request):
        message = request.POST['message']

        if not message:
            return Response({'error': 'Please provide a message.'}, status=status.HTTP_400_BAD_REQUEST)

        response_data = {'message':predict(message)}

        return Response(response_data, status=status.HTTP_200_OK)