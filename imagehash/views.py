import requests
import hashlib
from PIL import Image
import imagehash
from io import BytesIO
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import ImageData
from .serializers import ImageDataSerializer

@api_view(['POST'])
def upload_image(request):
    image_url = request.data.get('image_url')
    if not image_url:
        return Response({'error': 'Image URL is required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Fetch the image
        response = requests.get(image_url)
        response.raise_for_status()

        # Calculate MD5
        md5_hash = hashlib.md5(response.content).hexdigest()

        # Calculate pHash
        image = Image.open(BytesIO(response.content))
        phash = str(imagehash.phash(image))

        # Save data
        image_data = ImageData.objects.create(image_url=image_url, md5_hash=md5_hash, phash=phash)
        serializer = ImageDataSerializer(image_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

# Generic Views for List, Retrieve, Update, Delete
class ImageDataListCreateView(generics.ListCreateAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer

class ImageDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageData.objects.all()
    serializer_class = ImageDataSerializer