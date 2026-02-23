"""
Image Generator node: Generates AI images using Google's Nano Banana Pro
(Gemini 2.5 Flash Image) model via a SEPARATE API key to avoid rate limits
on the main tweet generation key.
"""
import tempfile
import os
from google import genai
from app.models import BotState
from app.config import Config


def image_generator(state: BotState) -> dict:
    """
    Image generation node: Creates a cinematic AI image for the tweet
    using Google's Nano Banana Pro model.
    
    Uses a SEPARATE Gemini API key (GEMINI_IMAGE_API_KEY) so image
    generation calls don't count against the main tweet generation quota.
    
    Args:
        state: Current bot state containing the final_tweet
        
    Returns:
        Updated state with image_prompt and image_path fields
    """
    if not Config.ENABLE_IMAGE_GENERATION:
        print("🖼️  Image generation disabled in config.")
        return {"image_prompt": "", "image_path": ""}
    
    if not Config.GEMINI_IMAGE_API_KEY:
        print("⚠️  No GEMINI_IMAGE_API_KEY set. Skipping image generation.")
        return {"image_prompt": "", "image_path": ""}
    
    try:
        # Create a client with the SEPARATE image generation API key
        client = genai.Client(api_key=Config.GEMINI_IMAGE_API_KEY)
        
        # Build a cinematic image prompt from the tweet content
        image_prompt = (
            f"Create a stunning, hyper-realistic, cinematic wide-angle photograph "
            f"related to this AI/tech news: {state['final_tweet'][:200]}. "
            f"The image should be photorealistic, with dramatic volumetric lighting, "
            f"deep focus, futuristic sci-fi aesthetic, vibrant neon colors, "
            f"and absolutely NO text, words, letters, or UI elements in the image. "
            f"16:9 aspect ratio, 8K quality, professional photography."
        )
        
        print("🎨 Generating image with Nano Banana Pro...")
        
        response = client.models.generate_content(
            model=Config.IMAGE_MODEL,
            contents=[image_prompt],
        )
        
        # Extract and save the generated image
        image_path = ""
        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                # Save to temp file
                tmp_file = tempfile.NamedTemporaryFile(
                    delete=False, suffix=".png", prefix="xai_tweet_"
                )
                tmp_file.close()
                image.save(tmp_file.name)
                image_path = tmp_file.name
                print(f"✅ Image generated and saved: {tmp_file.name}")
                break
        
        if not image_path:
            print("⚠️  No image data in response. Posting without image.")
            
        return {
            "image_prompt": image_prompt[:500],
            "image_path": image_path,
        }
        
    except Exception as e:
        print(f"⚠️  Image generation failed: {str(e)}")
        # Don't set error — we still want to publish the tweet without image
        return {"image_prompt": "", "image_path": ""}
