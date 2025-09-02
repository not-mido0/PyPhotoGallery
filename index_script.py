
import os 
def create_index():
    num_files = len(os.listdir("images"))
    cnt =0
    first =1 
    last = 5
    with open(os.path.join("htmls", "index.html") , "w") as f:
        f.write("<html>\n")
        f.write("<h1><p  align=\"center\"> Gallery</p></h1>\n")
        f.write("<table>\n")
        for i in range(1, num_files+1):
            f.write("<tr>\n")
            if cnt >= last-1 :
                first = last 
                last = first + 4
            for j in range(first, last ):
                f.write("<td>\n")
                f.write(f"<a href=\"images/image_{j}.jpg.html\" target=\"_new\">")
                f.write(f"<img src=\"images/image_{j}.jpg\" style=\"max-width:70%; height:auto;\">")
                f.write("</a>\n")
                f.write("</td>\n")
                
                cnt += 1
            if cnt >= num_files :
                break
        f.write("</tr>\n")
        f.write("</table>\n")
        f.write("</html>\n")
