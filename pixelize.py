from PIL import Image


def convert_to_black_and_white(input_image_path, output_image_path, threshold=128):
  """
  Converts an image to black and white with only "on" and "off" pixels.

  Args:
    input_image_path: Path to the input image file.
    output_image_path: Path to save the converted image.
    threshold: Grayscale value above which pixels are considered "on".

  Returns:
    list: A list of 0s and 1s representing the black and white pixel values.
  """
  img = Image.open(input_image_path)
  img = img.convert("L")  # Convert to grayscale

  # Create a black and white image
  bw_img = Image.new("1", img.size)  # 1 for binary mode

  pixel_array = []
  for x in range(img.width):
    for y in range(img.height):
      pixel_value = img.getpixel((x, y))
      bw_img.putpixel((x, y), 0 if pixel_value < threshold else 255)
      pixel_array.append(1 if pixel_value >= threshold else 0)

  bw_img.save(output_image_path)

  return pixel_array

# Example usage
input_image_path = "img.png"
output_image_path = "black_and_white.bmp"
pixel_array = convert_to_black_and_white(input_image_path, output_image_path)
print(pixel_array)