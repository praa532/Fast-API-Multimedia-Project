from dotenv import load_dotenv
import os
from imagekitio import ImageKit

# Load environment variables from .env file for configuration
load_dotenv()


# Configure ImageKit with credentials from environment variables
imagekit = ImageKit(
    private_key=os.getenv("IMAGEKIT_PRIVATE_KEY"), 
    public_key=os.getenv("IMAGEKIT_PUBLIC_KEY"),
    url_endpoint=os.getenv("IMAGEKIT_URL"),
)