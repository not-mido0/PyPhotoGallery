import os 
import index_script
_image = "images"

for file_name in os.listdir(_image):
    if file_name.endswith('.jpg'):
        content_to_add = f"""<p align="center">
<a href="{file_name}" target="_new">
    <img src="{file_name}" style="max-width:70%; height:auto;">
   </a>
    </p>

    <p align="center">
    <a href="index.html" >
     <button>back to gallery</button>
   </a> </p>"""
       
        folder = "htmls"
        os.makedirs(folder, exist_ok=True)
        
        name = file_name
        
        new_ = os.path.join(folder, f"{name}.html")
            
        with open(new_, "w") as f:
                f.write(content_to_add)
        
index_script.create_index()