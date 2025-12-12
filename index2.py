import cv2
import numpy as np

def create_gatsby_birthday_card(text_overlay, original_theme_text="The Gatsby Birthday"):
    """
    Creates a static Gatsby-themed birthday card image with custom text 
    using OpenCV, simulating a glamorous, gold-on-black Art Deco effect.
    """
    
    # 1. Image dimensions and dark background
    width, height = 1000, 700
    # Create a dark (almost black) canvas
    img = np.zeros((height, width, 3), dtype=np.uint8) 

    # 2. Define colors (BGR format: Blue, Green, Red)
    # A rich Gold color
    GOLD = (0, 215, 255) 

    # 3. Define text properties
    # Using a simple script font to simulate the Art Deco style
    font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX 
    thickness = 3
    
    # --- Add "The Gatsby Birthday" theme text (smaller, top) ---
    text_size_theme = 1.2
    (text_w_t, text_h_t), _ = cv2.getTextSize(original_theme_text, font, text_size_theme, thickness)
    x_theme = (width - text_w_t) // 2
    y_theme = 150
    cv2.putText(img, original_theme_text, (x_theme, y_theme), font, text_size_theme, GOLD, thickness, cv2.LINE_AA)
    
    # --- Add custom birthday text: "happy 18 maisarah" (large, center) ---
    text_to_add = text_overlay
    text_size_main = 3.0
    (text_w_m, text_h_m), _ = cv2.getTextSize(text_to_add, font, text_size_main, thickness)
    x_main = (width - text_w_m) // 2
    y_main = height // 2 + text_h_m // 2 - 20 # Centered slightly above middle

    # Text shadow/outline for a richer, embossed effect
    shadow_offset = 5
    cv2.putText(img, text_to_add, (x_main + shadow_offset, y_main + shadow_offset), font, text_size_main, (50, 50, 50), thickness * 2, cv2.LINE_AA)
    
    # Main gold text
    cv2.putText(img, text_to_add, (x_main, y_main), font, text_size_main, GOLD, thickness, cv2.LINE_AA)

    # 4. Simulate a "Wonderful Effect" (Art Deco frame and subtle glitter)
    
    # Add a thin gold border/frame for an Art Deco touch
    border_width = 30
    cv2.rectangle(img, (border_width // 2, border_width // 2), 
                  (width - border_width // 2, height - border_width // 2), 
                  GOLD, border_width // 4)
    
    # Add a slight random noise layer for a "glitter" or film grain effect
    noise = np.random.randint(0, 30, (height, width, 3), dtype=np.uint8)
    img = cv2.add(img, noise)

    return img

# --- Execution ---
text_for_maisarah = "happy 18 maisarah"
final_image = create_gatsby_birthday_card(text_for_maisarah)

# Save the resulting image
output_filename = "gatsby_birthday_maisarah.png"
cv2.imwrite(output_filename, final_image)

print(f"Successfully created a Gatsby-themed image with your text.")
print(f"The image has been saved to the current directory as: {output_filename}")