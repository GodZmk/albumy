import os
from dotenv import load_dotenv
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()

# Reference: Azure Computer Vision SDK v0.9.1 implementation
class azureAPI:
    def __init__(self):
        try:
            endpoint = os.environ["VISION_ENDPOINT"]
            key = os.environ["VISION_KEY"]
        except KeyError:
            print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
            print("Set them before running this sample.")
            exit()

        self.client = ComputerVisionClient(
            endpoint=endpoint,
            credentials=CognitiveServicesCredentials(key)
        )

    def analyze_image(self, image_path):
        try:
            with open(image_path, 'rb') as image_file:
                # Using the older API's analyze_image method
                result = self.client.analyze_image_in_stream(
                    image=image_file,
                    visual_features=['Description', 'Tags']
                )

            # Extract description and tags from the response
            description = result.description.captions[0].text if result.description.captions else ""
            tags = [tag.name for tag in result.tags]

            return description, tags
        except Exception as e:
            print(f"Error analyzing image: {str(e)}")
            return "", []




