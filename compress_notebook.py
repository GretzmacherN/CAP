import json
import base64
from io import BytesIO
from PIL import Image
#input_file = "2_Celltype_ID.ipynb"
#output_file = "2_Celltype_ID_github.ipynb"
input_file = "3_Epi_Recluster.ipynb"
output_file = "3_Epi_Recluster_github.ipynb"

# How much to reduce the embedded images
scale = 0.3
quality = 85

with open(input_file, "r", encoding="utf-8") as f:
    notebook = json.load(f)
n_images = 0
original_bytes = 0
new_bytes = 0

for cell in notebook["cells"]:
    for output in cell.get("outputs", []):
        data = output.get("data", {})

        if "image/png" not in data:
            continue

        png_data = base64.b64decode(data["image/png"])
        original_bytes += len(png_data)

        image = Image.open(BytesIO(png_data))

        # Resize
        new_width = max(1, int(image.width * scale))
        new_height = max(1, int(image.height * scale))

        image = image.resize(
            (new_width, new_height),
            Image.Resampling.LANCZOS)

        # Compress as PNG
        buffer = BytesIO()
        image.save(buffer, format="PNG", optimize=True)
        compressed = buffer.getvalue()
        new_bytes += len(compressed)

        data["image/png"] = base64.b64encode(compressed).decode("ascii")
        n_images += 1

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(notebook, f, ensure_ascii=False)

print(f"Processed images: {n_images}")
print(f"Original PNG data: {original_bytes / 1024**2:.1f} MB")
print(f"New PNG data:      {new_bytes / 1024**2:.1f} MB")
print(f"Created: {output_file}")